import pytest
import zipfile
import io
from app.github.validator import validate_github_url
from app.uploads.security import is_safe_zip

def test_github_url_validator():
    # Valid
    valid, owner, repo, err = validate_github_url("https://github.com/torvalds/linux")
    assert valid is True
    assert owner == "torvalds"
    assert repo == "linux"

    # Valid with .git
    valid2, owner2, repo2, _ = validate_github_url("https://github.com/facebook/react.git")
    assert valid2 is True
    assert owner2 == "facebook"
    assert repo2 == "react"

    # Invalid host (SSRF risk)
    invalid, _, _, err = validate_github_url("https://malicious-domain.com/evil/repo")
    assert invalid is False

    # Path traversal attack
    invalid2, _, _, _ = validate_github_url("https://github.com/../etc/passwd")
    assert invalid2 is False

def test_zip_security_path_traversal():
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as zf:
        # Dangerous path traversal entry
        zf.writestr("../../etc/passwd", "root:x:0:0")

    zip_file = zipfile.ZipFile(buffer, "r")
    is_safe, err_msg = is_safe_zip(zip_file, "/tmp/target")
    assert is_safe is False
    assert "traversal" in err_msg.lower() or "unsafe" in err_msg.lower()
