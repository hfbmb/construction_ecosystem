from fastapi import HTTPException


class BaseException(HTTPException):
    code: int

    def __init__(
        self,
        *,
        msg: str = None,
        data: Any = None,
    ):
        self.msg = msg
        self.data = data



