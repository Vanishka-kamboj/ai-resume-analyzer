import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

ALLOWED_EXTENSIONS = {"pdf", "docx"}

MAX_CONTENT_LENGTH = 5 * 1024 * 1024

os.makedirs(UPLOAD_FOLDER, exist_ok=True)