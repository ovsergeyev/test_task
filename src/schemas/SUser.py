from pydantic import BaseModel


class SUser(BaseModel):
    username: str
    password: str
