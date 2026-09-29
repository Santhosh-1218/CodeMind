import pytest
from app.analysis.deduplicator import deduplicate_findings
from app.analysis.scorer import calculate_deterministic_scores

def test_deduplication():
    findings = [
        {
            "title": "SQL Injection",
            "category": "Security",
            "severity": "Critical",
            "file_path": "app/api.py",
            "line_number": 10,
            "snippet": "cursor.execute(query)",
            "confidence": 90,
            "evidence": ["AST Flag"]
        },
        {
            "title": "SQL Injection",
            "category": "Security",
            "severity": "Critical",
            "file_path": "app/api.py",
            "line_number": 10,
            "snippet": "cursor.execute(query)",
            "confidence": 95,
            "evidence": ["LLM Flag"]
        }
    ]

    deduped = deduplicate_findings(findings)
    assert len(deduped) == 1
    assert "AST Flag" in deduped[0]["evidence"]
    assert "LLM Flag" in deduped[0]["evidence"]

def test_deterministic_scoring():
    findings = [
        {"severity": "Critical", "category": "Security", "confidence": 100},
        {"severity": "High", "category": "Quality", "confidence": 100}
    ]
    overall, quality, security, maintainability, reliability = calculate_deterministic_scores(findings)
    assert security == 80.0
    assert quality == 88.0
    assert overall > 0.0 and overall <= 100.0
