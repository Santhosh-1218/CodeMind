import os
import io
import zipfile
import tempfile
from app.uploads.zip_handler import process_zip_upload

def test_safe_zip_extraction():
    temp_dir = tempfile.mkdtemp()
    
    # Create valid dummy zip in memory
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zf:
        zf.writestr("app/main.py", "print('hello world')")
        zf.writestr("README.md", "# Test Project")
        
    zip_bytes = zip_buffer.getvalue()
    success, msg = process_zip_upload(zip_bytes, temp_dir)
    assert success is True
    assert os.path.exists(os.path.join(temp_dir, "app/main.py"))
