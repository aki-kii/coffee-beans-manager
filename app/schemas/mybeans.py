from typing import Optional, List

from datetime import date, datetime

from pydantic import BaseModel, Field

from app.schemas.beans import Beans

class MybeansBase(BaseModel):
    beans_id: int = Field(default=1)
    got_date: date = Field(date.today())
    weight: float = Field(default=200.0)

class WeightUpdateRequest(BaseModel):
    use_weight: float = Field(default=20.0)

class RoastBase(BaseModel):
    roast_level: Optional[str] = Field(None, example="浅煎り")
    roasted_date: Optional[date] = Field(None)

class RoastUpdateRequest(RoastBase):
    pass

class GrindBase(BaseModel):
    grind_size: Optional[str] = Field(None, example="粗挽き")
    grinded_date: Optional[date] = Field(None)

class GrindUpdateRequest(GrindBase):
    pass

class MybeansCreateRequest(MybeansBase, RoastBase, GrindBase):
    pass

class MybeansCreateResponse(MybeansCreateRequest):
    id: int

    class Config:
        orm_mode = True

class Mybeans(MybeansBase, RoastBase, GrindBase, Beans):
    id: int

    class Config:
        orm_mode = True