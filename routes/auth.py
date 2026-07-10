from fastapi import APIRouter
from models.user_model import users_collection
from schemas.user_schema import UserSignup
from utils.password import hash_password

router = APIRouter()


@router.post("/signup")
def signup(user: UserSignup):

    # Check if email already exists
    existing_user = users_collection.find_one({"email": user.email})

    if existing_user:
        return {
            "success": False,
            "message": "Email already registered"
        }

    # Convert Pydantic model to dictionary
    user_data = user.model_dump()
    user_data["password"] = hash_password(user.password)

    # Store in MongoDB
    users_collection.insert_one(user_data)

    return {
        "success": True,
        "message": "User registered successfully"
    }