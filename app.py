from fastapi import FastAPI
from routes.auth import router as auth_router

app = FastAPI(
    title="AI Resume Analyzer API",
    version="1.0"
)

app.include_router(auth_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Resume Analyzer",
        "developer": "Pramod",
        "status": "Running Successfully"
    }