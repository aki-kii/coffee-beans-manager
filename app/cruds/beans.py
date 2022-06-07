from tkinter import W
from typing import List, Tuple, Optional

from sqlalchemy import select
from sqlalchemy.engine import Result

from sqlalchemy.ext.asyncio import AsyncSession

from datetime import date

import app.models.beans as beans_model
import app.schemas.beans as beans_schema

async def create_beans(
    db: AsyncSession, beans_create: beans_schema.BeansCreateRequest
) -> beans_model.Beans:
    beans = beans_model.Beans(**beans_create.dict())
    db.add(beans)
    await db.commit()
    await db.refresh(beans)
    return beans

async def get_beans_list(db: AsyncSession) -> List[Tuple[int, str, str, str]]:
    result: Result = await(
        db.execute(
            select(
                beans_model.Beans.id,
                beans_model.Beans.shop,
                beans_model.Beans.country,
                beans_model.Beans.origin
            )
        )
    )
    return result.all()

async def get_beans(db: AsyncSession, beans_id: int) -> Optional[beans_model.Beans]:
    result: Result = await db.execute(
        select(beans_model.Beans).filter(beans_model.Beans.id == beans_id)
    )
    beans: Optional[Tuple[beans_model.Beans]] = result.first()
    return beans[0] if beans is not None else None

async def update_beans(
    db: AsyncSession, beans_create: beans_schema.BeansCreateRequest, original: beans_model.Beans
) -> beans_model.Beans:
    if beans_create.shop is not None: original.shop = beans_create.shop
    if beans_create.country is not None: original.country = beans_create.country
    if beans_create.origin is not None: original.origin = beans_create.origin
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original

async def delete_beans(db: AsyncSession, original: beans_model.Beans) -> None:
    await db.delete(original)
    await db.commit()
