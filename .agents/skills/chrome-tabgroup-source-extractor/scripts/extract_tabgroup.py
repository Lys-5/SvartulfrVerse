#!/usr/bin/env python3
"""
Chrome TabGroup Source Extractor
Extracts saved tab groups, URLs, and titles directly from Chrome Sync LevelDB files.
Zero-disruption: operates on disk without restarting Chrome, bypassing CDP port locks.
"""

import os
import sys
import re
import glob
import json
import argparse

def get_default_chrome_sync_dir():
    """Locate the Chrome Sync LevelDB directory on Windows, macOS, or Linux."""
    if sys.platform == "win32":
        local_app_data = os.environ.get("LOCALAPPDATA", os.path.expanduser("~\\AppData\\Local"))
        sync_dir = os.path.join(local_app_data, "Google", "Chrome", "User Data", "Default", "Sync Data", "LevelDB")
    elif sys.platform == "darwin":
        sync_dir = os.path.expanduser("~/Library/Application Support/Google/Chrome/Default/Sync Data/LevelDB")
    else:
        sync_dir = os.path.expanduser("~/.config/google-chrome/Default/Sync Data/LevelDB")
    return sync_dir

def read_all_leveldb_files(sync_dir):
    """Read all .ldb and .log files in the Sync LevelDB directory."""
    files = glob.glob(os.path.join(sync_dir, "*.ldb")) + glob.glob(os.path.join(sync_dir, "*.log"))
    combined = bytearray()
    for f in sorted(files, key=os.path.getmtime, reverse=True):
        try:
            with open(f, "rb") as fh:
                combined.extend(fh.read())
        except Exception:
            continue
    return bytes(combined)

def discover_groups(data):
    """Find all saved tab groups in the LevelDB sync dump."""
    groups = {}
    guid_pattern = rb"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}"
    matches = list(re.finditer(guid_pattern, data))
    
    for m in matches:
        guid = m.group(0).decode("ascii")
        start = max(0, m.start() - 250)
        end = min(len(data), m.end() + 250)
        window = data[start:end]
        
        # Look for group metadata signatures
        if b"saved_tab_group" in window or b"group" in window:
            strings = re.findall(rb"[\x20-\x7e]{3,50}", window)
            decoded = [s.decode("latin1") for s in strings]
            for s in decoded:
                if s not in guid and not s.startswith("http") and not s.startswith("saved_tab") and len(s) >= 3:
                    if guid not in groups:
                        groups[guid] = s
    return groups

def extract_tabs_for_group(data, group_guid):
    """Extract all tab URLs and titles associated with a specific tab group GUID."""
    target = group_guid.encode("ascii")
    guid_pattern = rb"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}"
    matches = []
    idx = 0
    while True:
        pos = data.find(target, idx)
        if pos == -1:
            break
        matches.append(pos)
        idx = pos + len(target)

    tabs = []
    seen_urls = set()

    for pos in matches:
        start = max(0, pos - 200)
        end = min(len(data), pos + 1200)
        snippet = data[start:end]

        urls = re.findall(rb"https?://[^\x00-\x20\x7f-\xff\"\'<>]+", snippet)
        for u_bytes in urls:
            u_offset = snippet.find(u_bytes)
            # Ensure the target GUID is closer to this URL than any other GUID
            between = snippet[min(pos - start, u_offset):max(pos - start, u_offset)]
            other_guids = [g for g in re.findall(guid_pattern, between) if g != target]
            if other_guids:
                continue

            url = u_bytes.decode("latin1", errors="ignore")
            # Normalize trailing garbage
            url = re.sub(r"[\),;]+$", "", url)
            if url in seen_urls:
                continue

            # Extract title nearby
            title = ""
            if u_offset != -1:
                t_window = snippet[max(0, u_offset - 250):u_offset]
                printable = re.findall(rb"[\x20-\x7e]{3,80}", t_window)
                candidates = [
                    p.decode("latin1") for p in printable 
                    if not p.startswith(b"http") and not p.startswith(b"uuid") and p != target and not re.match(guid_pattern, p)
                ]
                if candidates:
                    title = candidates[-1]

            seen_urls.add(url)
            tabs.append({
                "url": url,
                "title": title or url
            })

    return tabs

def main():
    parser = argparse.ArgumentParser(description="Extract tab groups and URLs from Chrome Sync LevelDB files.")
    parser.add_argument("--group", "-g", type=str, default=None, help="Name or substring of the tab group to extract (e.g. 'RPG Source').")
    parser.add_argument("--guid", type=str, default=None, help="Direct GUID of the tab group.")
    parser.add_argument("--sync-dir", "-d", type=str, default=None, help="Custom path to Chrome Sync Data/LevelDB directory.")
    parser.add_argument("--format", "-f", choices=["json", "table", "markdown", "list"], default="table", help="Output format.")
    parser.add_argument("--list-groups", "-l", action="store_true", help="List all discovered tab groups.")
    args = parser.parse_args()

    sync_dir = args.sync_dir or get_default_chrome_sync_dir()
    if not os.path.exists(sync_dir):
        sys.stderr.write(f"Error: Chrome Sync LevelDB directory not found at {sync_dir}\n")
        sys.exit(1)

    data = read_all_leveldb_files(sync_dir)
    if not data:
        sys.stderr.write("Error: Could not read LevelDB sync data files.\n")
        sys.exit(1)

    groups = discover_groups(data)

    if args.list_groups:
        print(f"Discovered {len(groups)} Tab Groups:")
        for guid, name in groups.items():
            print(f"- [{guid}] {name}")
        return

    target_guid = args.guid
    target_name = args.group

    if not target_guid and target_name:
        for guid, name in groups.items():
            if target_name.lower() in name.lower():
                target_guid = guid
                target_name = name
                break

    # Fallback search if title not in discovered groups
    if not target_guid and target_name:
        pos = data.find(target_name.encode("utf-8"))
        if pos != -1:
            guid_match = re.search(rb"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}", data[max(0, pos-300):min(len(data), pos+300)])
            if guid_match:
                target_guid = guid_match.group(0).decode("ascii")

    if not target_guid:
        if target_name:
            sys.stderr.write(f"Error: Group matching '{target_name}' not found.\n")
        else:
            sys.stderr.write("Error: Please specify --group or --guid, or run with --list-groups.\n")
        sys.exit(1)

    tabs = extract_tabs_for_group(data, target_guid)

    if args.format == "json":
        print(json.dumps({"group": target_name or target_guid, "guid": target_guid, "tabs": tabs}, indent=2))
    elif args.format == "markdown":
        print(f"### Tab Group: {target_name or target_guid} ({len(tabs)} tabs)\n")
        print("| # | Title | URL |")
        print("|---|-------|-----|")
        for i, t in enumerate(tabs, 1):
            print(f"| {i} | {t['title']} | `{t['url']}` |")
    elif args.format == "list":
        for t in tabs:
            print(t["url"])
    else:
        print(f"\n=== Tab Group: {target_name or target_guid} ({len(tabs)} tabs) ===")
        for i, t in enumerate(tabs, 1):
            print(f"{i:2d}. {t['title']} -> {t['url']}")

if __name__ == "__main__":
    main()
