from pydantic import BaseModel
from datetime import datetime


class SAccessToken(BaseModel):
    access_token: str
    token_type: str
    expire: datetime
