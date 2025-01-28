from src.services.user_service import UserService
from src.models.user_model import User
from src.database.database import get_db
from src.repositories.user_repository import UserRepository


def get_user_service():
    user_repository = UserRepository(User, get_db)
    user_service = UserService(user_repository)
    return user_service
