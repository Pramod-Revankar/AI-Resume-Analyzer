from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parent

model = joblib.load(BASE_DIR / "model.pkl")
vectorizer = joblib.load(BASE_DIR / "vectorizer.pkl")


def predict_job_role(skills):
    text = " ".join(skills)

    vector = vectorizer.transform([text])

    prediction = model.predict(vector)[0]
    confidence = model.predict_proba(vector).max()

    return {
        "role": prediction,
        "confidence": round(confidence * 100, 2)
    }