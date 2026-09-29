import sqlite3
import os

db_paths = [
    "c:/Users/so143/Desktop/CodeMind/data/codemind.db",
    "data/codemind.db",
    "backend/data/codemind.db"
]

for db_path in db_paths:
    if os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        
        # Check existing columns in findings table
        c.execute("PRAGMA table_info(findings)")
        columns = [row[1] for row in c.fetchall()]
        
        if "line_end" not in columns:
            print(f"Adding line_end to {db_path}")
            c.execute("ALTER TABLE findings ADD COLUMN line_end INTEGER")
            
        if "confidence" not in columns:
            print(f"Adding confidence to {db_path}")
            c.execute("ALTER TABLE findings ADD COLUMN confidence INTEGER DEFAULT 90")
            
        if "evidence" not in columns:
            print(f"Adding evidence to {db_path}")
            c.execute("ALTER TABLE findings ADD COLUMN evidence TEXT")
            
        conn.commit()
        conn.close()
        print(f"Successfully migrated schema for {db_path}")
