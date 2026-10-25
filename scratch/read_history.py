import sqlite3
import datetime

conn = sqlite3.connect(r"E:\repository\SvartulfrVerse\scratch\History_copy")
cursor = conn.cursor()

# Chrome timestamp is microseconds since 1601-01-01 UTC
def chrome_time_to_dt(ts):
    if not ts:
        return ""
    try:
        return (datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=ts)).strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        return str(ts)

cursor.execute("""
    SELECT id, url, title, visit_count, last_visit_time
    FROM urls
    ORDER BY last_visit_time DESC
    LIMIT 40
""")

rows = cursor.fetchall()
print(f"Latest {len(rows)} visits in Chrome History:")
for r in rows:
    dt = chrome_time_to_dt(r[4])
    print(f"[{dt}] {r[2]}")
    print(f"       {r[1]}")

conn.close()
