import pytest
from app.analysis.evidence_verifier import verify_findings

def test_evidence_verification_positive():
    files_data = [
        {
            "path": "app/checkout.py",
            "language": "Python",
            "content": "import sqlite3\ndef checkout(user_id):\n    cursor.execute(f'SELECT * FROM users WHERE id = {user_id}')\n",
            "size": 100
        }
    ]
    raw_findings = [
        {
            "title": "SQL Injection",
            "category": "Security",
            "severity": "Critical",
            "file_path": "app/checkout.py",
            "line_number": 3,
            "snippet": "cursor.execute(f'SELECT * FROM users WHERE id = {user_id}')",
            "description": "SQL Injection vulnerability",
            "fix_recommendation": "Use parameterized queries"
        }
    ]

    verified = verify_findings(files_data, raw_findings)
    assert len(verified) == 1
    assert verified[0]["confidence"] >= 90
    assert any("Confirmed file existence" in ev for ev in verified[0]["evidence"])

def test_evidence_verification_unverified_file():
    files_data = [
        {
            "path": "app/checkout.py",
            "language": "Python",
            "content": "print('hello')",
            "size": 14
        }
    ]
    raw_findings = [
        {
            "title": "Hallucinated Issue",
            "category": "Security",
            "severity": "High",
            "file_path": "non_existent_file.py",
            "line_number": 10,
            "snippet": "fake code",
            "description": "Fake issue"
        }
    ]

    verified = verify_findings(files_data, raw_findings)
    assert len(verified) == 1
    assert verified[0]["confidence"] <= 40
    assert "Manual Review Recommended" in verified[0]["title"]
