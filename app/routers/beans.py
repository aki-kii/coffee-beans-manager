from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import app.schemas.beans as beans_schema
import app.cruds.beans as beans_crud
from app.database import get_db

router = APIRouter()


@router.get("/beans", response_model=List[beans_schema.Beans], tags=['Beans'])
async def list_beans(db: AsyncSession = Depends(get_db)):
    """
    登録されているコーヒー豆の一覧を返す
    """
    return await beans_crud.get_beans_list(db)

@router.post("/beans", response_model=beans_schema.BeansCreateResponse, tags=['Beans'])
async def create_beans(
    beans_body: beans_schema.BeansCreateRequest, db: AsyncSession = Depends(get_db)
):
    """
    コーヒー豆を登録する
    - **shop**: 登録するコーヒー豆の販売店舗名
    - **country**: 登録するコーヒー豆の原産国
    - **origin**: 登録するコーヒー豆の産地情報
    """
    return await beans_crud.create_beans(db, beans_body)


@router.put("/beans/{beans_id}", response_model=beans_schema.BeansCreateResponse, tags=['Beans'])
async def update_mybeans(
    beans_id: int, beans_body: beans_schema.BeansCreateRequest, db: AsyncSession = Depends(get_db)
):
    """
    登録されているコーヒー豆の情報を更新する
    - **shop**: (Optional) 更新するコーヒー豆の販売店舗名
    - **country**: (Optional) 更新するコーヒー豆の原産国
    - **origin**: (Optional) 更新するコーヒー豆の産地情報
    """
    beans = await beans_crud.get_beans(db, beans_id=beans_id)
    if beans is None:
        raise HTTPException(status_code=404, detail="This beans is not found.")

    return await beans_crud.update_beans(db, beans_body, original=beans)

@router.delete("/beans/{mybeans_id}", response_model=None, tags=['Beans'])
async def delete_mybeans(beans_id: int, db: AsyncSession = Depends(get_db)):
    """
    登録されているコーヒー豆を削除する
    """
    beans = await beans_crud.get_beans(db, beans_id=beans_id)
    if beans is None:
        raise HTTPException(status_code=404, detail="This beans is not found")

    return await beans_crud.delete_beans(db, original=beans)