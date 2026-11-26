from pathlib import Path

final_dir = Path('FINAL')
opt_dir = Path('lorebooks/optimized')

for opt_file in opt_dir.glob('*.json'):
    f_file = final_dir / opt_file.name
    if not f_file.exists():
        print(f"Missing in FINAL/: {f_file.name}")
        continue
    c1 = f_file.read_bytes()
    c2 = opt_file.read_bytes()
    if c1 == c2:
        print(f"[OK] {opt_file.name}: 100% byte-for-byte identical ({len(c1)} bytes)")
    else:
        print(f"[MISMATCH] {opt_file.name}: FINAL ({len(c1)} bytes) != optimized ({len(c2)} bytes)")
