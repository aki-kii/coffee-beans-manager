from typing import Optional

from pydantic import BaseModel, Field

class BeansBase(BaseModel):
    shop: Optional[str] = Field(None, example="カルディコーヒーファーム")
    country: Optional[str] = Field(None, example="エチオピア")
    origin: Optional[str] = Field(None, example=None)

class BeansCreateRequest(BeansBase):
    pass

class BeansCreateResponse(BeansCreateRequest):
    id: int

    class Config:
        orm_mode = True

class Beans(BeansBase):
    id: int

    class Config:
        orm_mode = True