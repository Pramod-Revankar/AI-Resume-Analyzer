import os
from ml.parser import extract_text


UPLOAD_FOLDER = "uploads"


def save_resume(file):

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    extracted_text = extract_text(file_path)

    return {
        "filename": file.filename,
        "text": extracted_text
    }