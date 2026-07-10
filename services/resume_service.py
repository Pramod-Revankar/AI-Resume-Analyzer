from ml.parser import extract_text
from ml.skill_extractor import extract_skills
from ml.ats_score import calculate_ats_score
from ml.predictor import predict_job_role
import os
import joblib

UPLOAD_FOLDER = "uploads"

REQUIRED_SKILLS = [
    "Python",
    "FastAPI",
    "MongoDB",
    "React",
    "Git",
    "Docker",
    "AWS",
    "SQL"
]


def save_resume(file):

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    text = extract_text(file_path)

    skills = extract_skills(text)

    ats = calculate_ats_score(
        skills,
        REQUIRED_SKILLS
    )
    prediction = predict_job_role(skills)

    recommendation = "Excellent Resume"

    if ats["ats_score"] < 60:
        recommendation = "Needs significant improvement."

    elif ats["ats_score"] < 80:
        recommendation = "Good resume. Add missing skills."


    return {
        "filename": file.filename,
        "skills": skills,
        "ats_score": ats["ats_score"],
        "matched_skills": ats["matched_skills"],
        "missing_skills": ats["missing_skills"],
        "recommendation": recommendation,
        "predicted_role": prediction["role"],
        "job_role_prediction": prediction ,  
        "confidence": prediction["confidence"]
    }