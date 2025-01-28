import uuid

from pydantic import BaseModel, Field
from datetime import datetime

from src.schemas.base_schema import Base
from src.common.enums import UserRoles


class UserSchema(BaseModel):
    id: uuid.UUID = Field(..., description='username of a user', max_length=100)

    # class Config:
    #     extra = "allow"


class Individual(BaseModel):
    username: str = Field(..., description='username of a individual', max_length=100)
    first_name: str = Field(..., description='first_name of a individual', max_length=100)
    sur_name: str = Field(..., description='sur_name of a individual', max_length=100)
    last_name: str = Field(..., description='last_name of a individual', max_length=100)
    phone: str = Field(..., description='phone number of a individual', max_length=100)
    email: str = Field(..., description='email of a individual', max_length=100)
    # avatar: str = Field(None, description='avatar of an individual', max_length=100)
    password: str = Field(..., description='password of a individual', max_length=100)
    # salt: str = Field(..., description='salt of an individual', max_length=100)
    # active: bool = Field(..., description='status of an individual')
    # online: bool = Field(..., description='online/offline of an individual')
    # created_at: datetime = Field(..., description='created_at of an individual')
    # last_login_time: datetime = Field(..., description='last_login_time of an individual')

    class Config:
        json_schema_extra = {
            "example": {
                "username": "JohnDoe",
                "first_name": "John",
                "sur_name":  "D",
                "last_name": "Doe",
                "email": "john.doe@example.com",
                "phone": "123-456-7890",
                "password": "a1s8d0f0f",
                "reset_password": "a1s8d0f0f"
            }
        }


class ShowIndividual(BaseModel):
    id: uuid.UUID = Field(..., description='username of a user', max_length=100)
    username: str = Field(..., description='username of a user', max_length=100)
    email: str = Field(..., description='username of a user', max_length=100)


class Entity(BaseModel):
    organization_name: str = Field(..., description='organization_name of an entity', max_length=100)
    bin: str = Field(..., description='bin of an entity', max_length=100)
    # address: str = Field(..., description='address of an entity', max_length=100)
    # city: str = Field(..., description='city of an entity', max_length=100)
    # country: str = Field(..., description='country of an entity', max_length=100)
    # is_superuser: bool = Field(..., description='is superuser entity')
    # status: int = Field(..., description='status of an entity')
    # online: bool = Field(..., description='online/offline of an entity')
    first_name: str = Field(..., description='first_name of a entity', max_length=100)
    sur_name: str = Field(..., description='sur_name of a entity', max_length=100)
    last_name: str = Field(..., description='last_name of a entity', max_length=100)
    phone: str = Field(..., description='phone number of a entity', max_length=100)
    email: str = Field(..., description='email of a entity', max_length=100)
    # avatar: str = Field(..., description='avatar of an entity', max_length=100)
    password: str = Field(..., description='password of a entity', max_length=100)
    # salt: str = Field(..., description='salt of an entity', max_length=100)
    role: UserRoles = Field(..., description='role of an entity', max_length=100)
    field: str = Field(None, description='role of an entity', max_length=100)
    # website: str = Field(..., description='website of an entity', max_length=100)
    # description: str = Field(..., description='description of organization', max_length=200)

    class Config:
        json_schema_extra = {
            "example": {
                "organization_name": "Lpp",
                "bin": "08GH0fd0dc",
                "first_name": "John",
                "sur_name": "D",
                "last_name": "Doe",
                "email": "john.doe@example.com",
                "phone": "123-456-7890",
                "role": "contractor",
                "password": "a1s8d0f0f",
                "reset_password": "a1s8d0f0f",
                "field": "sales_department"
            }
        }


class UserUpdate(BaseModel):
    username: str = Field(..., description='username of a user', max_length=100)
    email: str = Field(..., description='username of a user', max_length=100)


class ShowEntity(Base):
    id: uuid.UUID = Field(..., description='username of a user', max_length=100)
    organization_name: str = Field(..., description='organization_name of an entity', max_length=100)
    email: str = Field(..., description='username of a user', max_length=100)
