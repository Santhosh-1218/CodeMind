import asyncio
import os
import sys

# Add backend to path
sys.path.insert(0, os.path.abspath("backend"))

from app.db.database import init_db, SessionLocal
from app.models.user import User
from app.models.project import Project
from app.models.review import Review
from app.workers.review_worker import run_review_pipeline
from app.hindsight.client import hindsight_client

async def main():
    print("1. Initializing DB...")
    init_db()
    db = SessionLocal()

    # Find or create test user
    user = db.query(User).filter(User.email == "demo@codemind.dev").first()
    if not user:
        user = User(email="demo@codemind.dev", full_name="Demo Developer", provider="email")
        db.add(user)
        db.commit()
        db.refresh(user)

    project = Project(user_id=user.id, name="Test Vulnerable App", source_type="zip")
    db.add(project)
    db.commit()
    db.refresh(project)

    review = Review(project_id=project.id, user_id=user.id, status="Queued", status_message="E2E test starting...")
    db.add(review)
    db.commit()
    db.refresh(review)

    # Create dummy codebase with SQL injection & hardcoded key
    sample_dir = os.path.join("data", "sample_test_code")
    os.makedirs(os.path.join(sample_dir, "app"), exist_ok=True)

    with open(os.path.join(sample_dir, "app", "checkout.py"), "w") as f:
        f.write('''import sqlite3

API_KEY = "sk_live_99887766554433221100"

def get_user_data(user_input):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    # SQL injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()
''')

    print(f"2. Running CodeMind pipeline for review ID {review.id}...")
    await run_review_pipeline(review.id, sample_dir, "Test Vulnerable App")

    # Verify review outcome
    db.refresh(review)
    print("\n=== E2E REVIEW PIPELINE RESULT ===")
    print(f"Status: {review.status}")
    print(f"Quality Score: {review.quality_score}")
    print(f"Security Score: {review.security_score}")
    print(f"Files Analyzed: {review.file_count}")
    print(f"Critical Issues: {review.critical_count}")
    print(f"Hindsight Memories Recalled: {review.hindsight_memories_recalled}")
    print(f"Hindsight Learnings Retained: {review.hindsight_learnings_retained}")
    print(f"Findings Count: {len(review.findings)}")

    for idx, f in enumerate(review.findings, 1):
        print(f"\nFinding {idx}: [{f.severity}] {f.title} ({f.file_path}:L{f.line_number})")
        print(f"Description: {f.description[:100]}...")
        if f.memory_influenced:
            print(f"-> Memory Influenced: {f.hindsight_memory_text}")

    db.close()
    print("\nE2E Verification Complete!")

if __name__ == "__main__":
    asyncio.run(main())
