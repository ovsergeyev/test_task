from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime


class SFileStatus(BaseModel):
    upload_datetime: datetime
    processing_datetime: Optional[datetime] = None
    status: str
    result: Optional[Dict[str, int]] = None
