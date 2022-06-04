from typing import Optional

from pydantic import BaseModel, Field

class Beans(BaseModel):
    id: int
    shop: Optional[str] = Field(None, example="カルディコーヒーファーム")
    country: Optional[str] = Field(None, example="エチオピア")
    origin: Optional[str] = Field(None, example="イルガチェフェ地方")