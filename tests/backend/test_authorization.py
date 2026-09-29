import pytest
import uuid
from fastapi.testclient import TestClient
from app.main import app
from app.models.user import User
from app.models.project import Project
from app.models.review import Review
from app.api.routes.auth import create_db_session

client = TestClient(app)

def test_review_ownership_authorization(test_db):
    db = test_db()
    try:
        uid_a = str(uuid.uuid4())[:8]
        uid_b = str(uuid.uuid4())[:8]

        # User A
        user_a = User(email=f"usera_{uid_a}@codemind.dev", full_name="User A", provider="email")
        db.add(user_a)
        db.commit()
        token_a = create_db_session(db, user_a.id)

        # User B
        user_b = User(email=f"userb_{uid_b}@codemind.dev", full_name="User B", provider="email")
        db.add(user_b)
        db.commit()
        token_b = create_db_session(db, user_b.id)

        # Create Project & Review for User A
        proj_a = Project(user_id=user_a.id, name="Project A", source_type="github")
        db.add(proj_a)
        db.commit()

        review_a = Review(project_id=proj_a.id, user_id=user_a.id, status="Completed", quality_score=90.0)
        db.add(review_a)
        db.commit()

        # 1. User A accesses User A's review -> 200 OK
        res_a = client.get(f"/api/reviews/{review_a.id}", cookies={"codemind_session": token_a})
        assert res_a.status_code == 200
        assert res_a.json()["id"] == review_a.id

        # 2. User B tries to access User A's review -> 404
        res_b = client.get(f"/api/reviews/{review_a.id}", cookies={"codemind_session": token_b})
        assert res_b.status_code == 404

        # 3. User B tries to access User A's review status -> 404
        status_b = client.get(f"/api/reviews/{review_a.id}/status", cookies={"codemind_session": token_b})
        assert status_b.status_code == 404

    finally:
        db.close()
