import sqlite3
import os

db_paths = ["data/codemind.db", "../data/codemind.db", "c:/Users/so143/Desktop/CodeMind/data/codemind.db"]
for path in db_paths:
    if os.path.exists(path):
        conn = sqlite3.connect(path)
        c = conn.cursor()
        c.execute("UPDATE reviews SET status = 'Failed', status_message = 'Review reset due to worker fix. Please resubmit.' WHERE status IN ('Queued', 'Downloading', 'Extracting')")
        conn.commit()
        print(f"Updated {c.rowcount} stuck reviews in {path}")
        conn.close()
