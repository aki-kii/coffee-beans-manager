from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import app.schemas.mybeans as mybeans_schema
import app.cruds.mybeans as mybeans_crud
from app.database import get_db

router = APIRouter()


@router.get("/mybeans", response_model=List[mybeans_schema.Mybeans], tags=['Mybeans'])
async def list_mybeans(db: AsyncSession = Depends(get_db)):
    """
    所持しているコーヒー豆の一覧を返す
    """
    return await mybeans_crud.get_mybeans_with_beans(db)

@router.post("/mybeans", response_model=mybeans_schema.MybeansCreateResponse, tags=['Mybeans'])
async def create_mybeans(
    mybeans_body: mybeans_schema.MybeansCreateRequest, db: AsyncSession = Depends(get_db)
):
    """
    所持しているコーヒー豆を登録する
    - **beans_id**: 所持しているコーヒー豆の登録番号(Beans.id)
    - **weight**: 所持しているコーヒー豆の重量
    - **got_date**: コーヒー豆を入手した日付
    - **roast_levele**: (Optional) 所持しているコーヒー豆の焙煎度合い
    - **roasted_date**: (Optional) 所持しているコーヒー豆を焙煎した日付
    - **grind_size**: (Optional) 所持しているコーヒー豆の挽き目
    - **grinded_date**: (Optional) 所持しているコーヒー豆を挽いた日付
    """
    return await mybeans_crud.create_mybeans(db, mybeans_body)

@router.put("/mybeans/{mybeans_id}", response_model=mybeans_schema.MybeansUpdateResponse, tags=['Mybeans'])
async def update_mybeans(
    mybeans_id: int, mybeans_body: mybeans_schema.MybeansUpdateRequest, db: AsyncSession = Depends(get_db)
):
    """
    所持しているコーヒー豆の情報を更新する
    - **beans_id**: (Optional) 所持しているコーヒー豆の登録番号(Beans.id)
    - **weight**: (Optional) 所持しているコーヒー豆の重量
    - **got_date**: (Optional) コーヒー豆を入手した日付
    - **roast_levele**: (Optional) 所持しているコーヒー豆の焙煎度合い
    - **roasted_date**: (Optional) 所持しているコーヒー豆を焙煎した日付
    - **grind_size**: (Optional) 所持しているコーヒー豆の挽き目
    - **grinded_date**: (Optional) 所持しているコーヒー豆を挽いた日付
    """
    mybeans = await mybeans_crud.get_mybeans(db, mybeans_id=mybeans_id)
    if mybeans is None:
        raise HTTPException(status_code=404, detail="This beans is not found.")

    return await mybeans_crud.update_mybeans(db, mybeans_body, original=mybeans)

@router.put("/mybeans/{mybeans_id}/use", response_model=mybeans_schema.Mybeans, tags=['Mybeans/Use'])
async def update_weight(
    mybeans_id: int, weight_body: mybeans_schema.WeightUpdateRequest, db: AsyncSession = Depends(get_db)
):
    """
    所持しているコーヒー豆を使用する(量を減らす)
    - **use_weight**: 使用したコーヒー豆の重量
    """
    mybeans = await mybeans_crud.get_mybeans(db, mybeans_id=mybeans_id)
    if mybeans is None:
        raise HTTPException(status_code=404, detail="This beans is not found.")

    return await mybeans_crud.update_weight(db, weight_body, original=mybeans)

@router.delete("/mybeans/{mybeans_id}", response_model=None, tags=['Mybeans'])
async def delete_mybeans(mybeans_id: int, db: AsyncSession = Depends(get_db)):
    """
    所持しているコーヒー豆を削除する
    """
    mybeans = await mybeans_crud.get_mybeans(db, mybeans_id=mybeans_id)
    if mybeans is None:
        raise HTTPException(status_code=404, detail="This beans is not found")

    return await mybeans_crud.delete_mybeans(db, original=mybeans)