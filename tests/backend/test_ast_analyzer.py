import pytest
from app.analysis.ast_analyzer import analyze_python_ast

def test_ast_sqli_positive():
    code = """
def get_user(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
"""
    findings = analyze_python_ast("app/db.py", code)
    assert len(findings) == 1
    assert findings[0]["rule_id"] == "AST-SEC-SQLI"
    assert findings[0]["severity"] == "Critical"
    assert findings[0]["line_number"] == 4

def test_ast_sqli_negative_parameterized():
    code = """
def get_user(user_id):
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))
"""
    findings = analyze_python_ast("app/db.py", code)
    assert len(findings) == 0

def test_ast_cmdi_positive():
    code = """
import os

def run_cmd(user_input):
    os.system("ls " + user_input)
"""
    findings = analyze_python_ast("app/utils.py", code)
    assert len(findings) == 1
    assert findings[0]["rule_id"] == "AST-SEC-CMDI"
    assert findings[0]["severity"] == "Critical"
    assert findings[0]["line_number"] == 5

def test_ast_eval_positive():
    code = """
def calc(expr):
    return eval(expr)
"""
    findings = analyze_python_ast("app/calc.py", code)
    assert len(findings) == 1
    assert findings[0]["rule_id"] == "AST-SEC-EVAL"
    assert findings[0]["severity"] == "High"
