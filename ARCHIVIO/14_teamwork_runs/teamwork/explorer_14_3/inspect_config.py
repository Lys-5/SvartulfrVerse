import json

with open("proxy/config_free_proxy.json", "r", encoding="utf-8") as f:
    cfg = json.load(f)

print(f"Host: {cfg.get('host')}:{cfg.get('port')}")
print(f"Cooldown: {cfg.get('cooldown_seconds')}s, Timeout: {cfg.get('timeout_seconds')}s")
print("\n--- CONFIGURED KEYS ---")
keys = cfg.get("keys", {})
for k, v in keys.items():
    if isinstance(v, list):
        print(f"  {k}: {len(v)} keys configured")
    else:
        print(f"  {k}: length={len(v)} chars, prefix={v[:6]}... suffix={v[-4:]}")

print("\n--- UPSTREAMS ---")
upstreams = cfg.get("upstreams", [])
for u in upstreams:
    models = u.get("models") or [u.get("model")]
    print(f"  P{u.get('priority'):02d} [{u.get('provider')}] ({u.get('key_name')}) -> {u.get('id')}: {models}")
