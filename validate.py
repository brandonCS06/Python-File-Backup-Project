import os
import re

def validate_Path(path):
    #Validate file paths#

    normalized = os.path.normpath(path)
    # Check for directory traversal attempts (..) but allow absolute paths
    if '..' in normalized:
        raise ValueError("Invalid path: potential directory traversal")
    return normalized

def validate_FileExtension(ext):
    #Validate file extensions to prevent malicious files#
    validExtensions = {'.txt','.jpg','.docx'}
    if not ext.lower() in validExtensions or not ext.startswith('.'):
        raise ValueError(f"Invalid file extension: {ext}. Allowed extensions are {', '.join(validExtensions)}")
    return ext.lower()


