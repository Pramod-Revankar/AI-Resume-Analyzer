from fastapi import APIRouter, UploadFile, File
from services.resume_service import save_resume

router = APIRouter()


@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    result = save_resume(file)

    return {
        "success": True,
        "data": result
    }