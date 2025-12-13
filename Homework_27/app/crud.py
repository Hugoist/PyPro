from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Item, ItemCreate, ItemUpdate


async def create_item(session: AsyncSession, item_data: ItemCreate, owner_id: int) -> Item:
    item = Item.model_validate(item_data)
    item.owner_id = owner_id
    session.add(item)
    await session.commit()
    await session.refresh(item)
    return item


async def get_item(session: AsyncSession, item_id: int) -> Optional[Item]:
    return await session.get(Item, item_id)


async def get_items(
        session: AsyncSession,
        skip: int = 0,
        limit: int = 100,
        owner_id: Optional[int] = None,
        q: Optional[str] = None,
        sort_by: str = "id",
        order: str = "asc",
) -> List[Item]:
    stmt = select(Item)
    if owner_id is not None:
        stmt = stmt.where(Item.owner_id == owner_id)
    if q:
        stmt = stmt.where(Item.title.ilike(f"%{q}%"))
    if hasattr(Item, sort_by):
        column = getattr(Item, sort_by)
        if order == "desc":
            column = column.desc()
        stmt = stmt.order_by(column)
    stmt = stmt.offset(skip).limit(limit)
    result = await session.execute(stmt)
    return result.scalars().all()


async def update_item(
        session: AsyncSession, item_id: int, item_data: ItemUpdate, current_user_id: int
) -> Optional[Item]:
    item = await session.get(Item, item_id)
    if not item or item.owner_id != current_user_id:
        return None
    for key, value in item_data.model_dump(exclude_unset=True).items():
        setattr(item, key, value)
    session.add(item)
    await session.commit()
    await session.refresh(item)
    return item


async def delete_item(session: AsyncSession, item_id: int, current_user_id: int) -> bool:
    item = await session.get(Item, item_id)
    if not item or item.owner_id != current_user_id:
        return False
    await session.delete(item)
    await session.commit()
    return True
