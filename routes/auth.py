from fastapi import APIRouter
from models.user_model import users_collection
from schemas.user_schema import UserSignup
from schemas.login_schema import UserLogin
from utils.password import hash_password, verify_password
from utils.jwt_handler import create_access_token

router = APIRouter()


@router.post("/signup")
def signup(user: UserSignup):

    existing_user = users_collection.find_one(
        {"email": user.email}
    )

    if existing_user:
        return {
            "success": False,
            "message": "Email already registered"
        }

    user_data = user.model_dump()

    user_data["password"] = hash_password(user.password)

    users_collection.insert_one(user_data)

    return {
        "success": True,
        "message": "User Registered Successfully"
    }


@router.post("/login")
def login(user: UserLogin):

    db_user = users_collection.find_one(
        {"email": user.email}
    )

    if not db_user:
        return {
            "success": False,
            "message": "User not found"
        }

    if not verify_password(
        user.password,
        db_user["password"]
    ):
        return {
            "success": False,
            "message": "Invalid password"
        }

    token = create_access_token(
        {
            "email": db_user["email"],
            "name": db_user["name"]
        }
    )

    return {
        "success": True,
        "message": "Login Successful",
        "access_token": token,
        "token_type": "Bearer"
    }