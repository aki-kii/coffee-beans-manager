from typing import Optional, List

from datetime import date, datetime

from pydantic import BaseModel, Field

from app.schemas.beans import BeansBase

class MybeansBase(BaseModel):
    roast_level: Optional[str] = Field(None, example="浅煎り")
    roasted_date: Optional[date] = Field(None)
    grind_size: Optional[str] = Field(None, example="粗挽き")
    grinded_date: Optional[date] = Field(None)

class WeightUpdateRequest(BaseModel):
    use_weight: float = Field(default=20.0, ge=0)

class MybeansCreateRequest(MybeansBase):
    beans_id: int = Field(default=1)
    got_date: date = Field(date.today())
    weight: float = Field(default=200.0, ge=0)

class MybeansCreateResponse(MybeansCreateRequest):
    id: int

    class Config:
        orm_mode = True

class MybeansUpdateRequest(MybeansBase):
    beans_id: Optional[int] = Field(default=1)
    got_date: Optional[date] = Field(date.today())
    weight: Optional[float] = Field(default=200.0, ge=0)

class MybeansUpdateResponse(MybeansUpdateRequest):
    id: int

    class Config:
        orm_mode = True

class Mybeans(MybeansBase, BeansBase):
    id: int
    got_date: date
    weight: float

    class Config:
        orm_mode = True