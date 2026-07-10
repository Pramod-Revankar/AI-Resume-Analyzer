import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_PATH = BASE_DIR / "dataset" / "job_roles.csv"

df = pd.read_csv(DATASET_PATH)

X = df["resume"]
y = df["role"]

vectorizer = TfidfVectorizer()

X_vector = vectorizer.fit_transform(X)

model = MultinomialNB()

model.fit(X_vector, y)

joblib.dump(model, "ml/model.pkl")
joblib.dump(vectorizer, "ml/vectorizer.pkl")

print("Model Trained Successfully")