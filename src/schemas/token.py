from datetime import datetime

from src.common.schemas.base_schema import Base


class GetSwaggerToken(Base):
    access_token: str
    token_type: str = 'Bearer'
    user: GetUserInfoNoRelation


class AccessTokenBase(Base):
    access_token: str
    access_token_type: str = 'Bearer'
    access_token_expire_time: datetime


class GetLoginToken(Base):
    refresh_token: str
    refresh_token_type: str = 'Bearer'
    refresh_token_expire_time: datetime
    user: GetUserInfoNoRelation


class GetNewToken(Base):
    refresh_token: str
    refresh_token_type: str = 'Bearer'
    refresh_token_expire_time: datetime
