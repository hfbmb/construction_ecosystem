from sqlalchemy.ext.asyncio import AsyncSession
from fast_captcha import text_captcha

from src.repositories.sqlalchemy_repository import ModelType
from src.models.user_model import User
from src.schemas.base_schema import PyModel
from src.services.base_service import BaseService
from src.common.jwt import get_hash_password
from src.common import constants
# from src.repositories.user_repository import user_repository


class UserService(BaseService):
    async def create(self, model: PyModel) -> ModelType:
        data = self.tide_up(model.model_dump())
        return await self.repository.create(data=data)

    @static
    def tide_up(self, user_data: dict) -> dict:
        salt = text_captcha(101)
        hashed_password = get_hash_password(user_data[constants.User.password]+salt)
        user_data[constants.User.password] = hashed_password
        user_data[constants.User.salt] = salt
        if constants.User.role in user_data and user_data[constants.User.role] == "founder":
            user_data[constants.User.is_superuser] = True
        return user_data




# user_service = UserService(user_repository)
