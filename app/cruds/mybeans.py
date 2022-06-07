from http.client import HTTPException
from typing import List, Tuple, Optional

from sqlalchemy import select
from sqlalchemy.engine import Result

from sqlalchemy.ext.asyncio import AsyncSession

from datetime import date

import app.models.mybeans as mybeans_model
import app.schemas.mybeans as mybeans_schema

async def create_mybeans(
    db: AsyncSession, mybeans_create: mybeans_schema.MybeansCreateRequest
) -> mybeans_model.Mybeans:
    mybeans = mybeans_model.Mybeans(**mybeans_create.dict())
    db.add(mybeans)
    await db.commit()
    await db.refresh(mybeans)
    return mybeans

async def get_mybeans_with_beans(db: AsyncSession) -> List[Tuple[int, str, str, str, float, str, date, str, date, date]]:
    result: Result = await(
        db.execute(
            select(
                mybeans_model.Mybeans.id,
                mybeans_model.Beans.shop.label("shop"),
                mybeans_model.Beans.country.label("country"),
                mybeans_model.Beans.origin.label("origin"),
                mybeans_model.Mybeans.weight,
                mybeans_model.Mybeans.roast_level,
                mybeans_model.Mybeans.roasted_date,
                mybeans_model.Mybeans.grind_size,
                mybeans_model.Mybeans.grinded_date,
                mybeans_model.Mybeans.got_date,
            ).outerjoin(mybeans_model.Beans)
        )
    )
    return result.all()

async def get_mybeans(db: AsyncSession, mybeans_id: int) -> Optional[mybeans_model.Mybeans]:
    result: Result = await db.execute(
        select(mybeans_model.Mybeans).filter(mybeans_model.Mybeans.id == mybeans_id)
    )
    mybeans: Optional[Tuple[mybeans_model.Mybeans]] = result.first()
    return mybeans[0] if mybeans is not None else None

async def update_mybeans(
    db: AsyncSession, mybeans_update: mybeans_schema.MybeansUpdateRequest, original: mybeans_model.Mybeans
) -> mybeans_model.Mybeans:
    if mybeans_update.beans_id is not None: original.beans_id = mybeans_update.beans_id
    if mybeans_update.weight is not None: original.weight = mybeans_update.weight
    if mybeans_update.roast_level is not None: original.roast_level = mybeans_update.roast_level
    if mybeans_update.roasted_date is not None: original.roasted_date = mybeans_update.roasted_date
    if mybeans_update.grind_size is not None: original.grind_size = mybeans_update.grind_size
    if mybeans_update.grinded_date is not None: original.grinded_date = mybeans_update.grinded_date
    if mybeans_update.got_date is not None: original.got_date = mybeans_update.got_date
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original

async def update_weight(
    db: AsyncSession, weight_update: mybeans_schema.WeightUpdateRequest, original: mybeans_model.Mybeans
) -> mybeans_model.Mybeans:
    if weight_update.use_weight <= original.weight:
        original.weight -= weight_update.use_weight

    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original

async def delete_mybeans(db: AsyncSession, original: mybeans_model.Mybeans) -> None:
    await db.delete(original)
    await db.commit()