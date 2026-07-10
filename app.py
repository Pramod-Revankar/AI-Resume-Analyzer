from fastapi import FastAPI, Depends
from routes.auth import router as auth_router
from dependencies.auth import verify_token
from routes.resume import router as resume_router



app = FastAPI(
    title="AI Resume Analyzer",
    version="1.0"
)

app.include_router(auth_router)
app.include_router(resume_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Resume Analyzer"
    }


@app.get("/profile")
def profile(user=Depends(verify_token)):
    return {
        "message": "Welcome",
        "user": user
    }