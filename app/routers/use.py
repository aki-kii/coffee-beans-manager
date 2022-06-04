from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import app.schemas.mybeans as mybeans_schema
import app.cruds.mybeans as mybeans_crud
from app.database import get_db

router = APIRouter()


@router.post("/mybeans/{mybeans_id}/use", response_model=mybeans_schema.MybeansCreateResponse)
async def update_weight(
    mybeans_id: int, mybeans_body: mybeans_schema.WeightUpdateRequest, db: AsyncSession = Depends(get_db)
):
    mybeans = await mybeans_crud.get_mybeans(db, mybeans_id=mybeans_id)
    if mybeans is None:
        raise HTTPException(status_code=404, detail="This beans is not found.")

    return await mybeans_crud.update_weight(db, mybeans_body, original=mybeans)