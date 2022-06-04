from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import app.schemas.mybeans as mybeans_schema
import app.cruds.mybeans as mybeans_crud
from app.database import get_db

router = APIRouter()


@router.get("/mybeans", response_model=List[mybeans_schema.Mybeans])
async def list_my_beans(db: AsyncSession = Depends(get_db)):
    return await mybeans_crud.get_mybeans_with_beans(db)

@router.post("/mybeans", response_model=mybeans_schema.MybeansCreateResponse)
async def create_my_beans(
    mybeans_body: mybeans_schema.MybeansCreateRequest, db: AsyncSession = Depends(get_db)
):
    return await mybeans_crud.create_mybeans(db, mybeans_body)


@router.put("/mybeans/{my_beans_id}", response_model=mybeans_schema.MybeansCreateResponse)
async def update_mybeans(
    mybeans_id: int, mybeans_body: mybeans_schema.MybeansCreateRequest, db: AsyncSession = Depends(get_db)
):
    mybeans = await mybeans_crud.get_mybeans(db, mybeans_id=mybeans_id)
    if mybeans is None:
        raise HTTPException(status_code=404, detail="This beans is not found.")

    return await mybeans_crud.update_mybeans(db, mybeans_body, original=mybeans)

@router.delete("/mybeans/{mybeans_id}", response_model=None)
async def delete_mybeans(mybeans_id: int, db: AsyncSession = Depends(get_db)):
    mybeans = await mybeans_crud.get_mybeans(db, mybeans_id=mybeans_id)
    if mybeans is None:
        raise HTTPException(status_code=404, detail="This beans is not found")

    return await mybeans_crud.delete_mybeans(db, original=mybeans)