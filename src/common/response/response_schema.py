from datetime import datetime
from typing import Any

from pydantic import BaseModel

from src.common.response.response_code import CustomResponseCode
from backend.app.core.conf import settings
from backend.app.utils.encoders import jsonable_encoder

_ExcludeData = set[int | str] | dict[int | str, Any]

__all__ = ['ResponseModel', 'response_base']


class ResponseBase:

    @staticmethod
    async def __response(
        *, res: CustomResponseCode = None, data: Any | None = None, exclude: _ExcludeData | None = None, **kwargs
    ) -> dict:
        if data is not None:
            custom_encoder = {datetime: lambda x: x.strftime(settings.DATETIME_FORMAT)}
            kwargs.update({'custom_encoder': custom_encoder})
            data = jsonable_encoder(data, exclude=exclude, **kwargs)
        return {'code': res.code, 'msg': res.msg, 'data': data}

    async def success(
        self,
        *,
        res: CustomResponseCode = CustomResponseCode.HTTP_200,
        data: Any | None = None,
        exclude: _ExcludeData | None = None,
        **kwargs
    ) -> dict:
        return await self.__response(res=res, data=data, exclude=exclude, **kwargs)

    async def fail(
        self,
        *,
        res: CustomResponseCode = CustomResponseCode.HTTP_400,
        data: Any = None,
        exclude: _ExcludeData | None = None,
        **kwargs
    ) -> dict:
        return await self.__response(res=res, data=data, exclude=exclude, **kwargs)


response_base = ResponseBase()
