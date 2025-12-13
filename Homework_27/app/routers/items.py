from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud
from app.database import get_session
from app.models import ItemRead, ItemCreate, ItemUpdate

router = APIRouter()


# TODO: create real auth
async def get_current_user_id() -> int:
    return 1


@router.post("/", response_model=ItemRead, status_code=status.HTTP_201_CREATED)
async def create_item(
        item_data: ItemCreate,
        session: AsyncSession = Depends(get_session),
        current_user_id: int = Depends(get_current_user_id),
):
    item = await crud.create_item(session, item_data, owner_id=current_user_id)
    return item


@router.get("/{item_id}", response_model=ItemRead)
async def read_item(
        item_id: int,
        session: AsyncSession = Depends(get_session),
):
    """Get item by ID"""
    item = await crud.get_item(session, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.get("/", response_model=List[ItemRead])
async def list_items(
        skip: int = 0,
        limit: int = 10,
        owner_id: Optional[int] = Query(None, description="Filter by owner id"),
        q: Optional[str] = Query(None, description="Search by title"),
        sort_by: str = Query("id", description="Field to sort by, e.g. id,title,price"),
        order: str = Query("asc", description="asc or desc"),
        session: AsyncSession = Depends(get_session),
):
    items = await crud.get_items(
        session,
        skip=skip,
        limit=limit,
        owner_id=owner_id,
        q=q,
        sort_by=sort_by,
        order=order,
    )
    return items


@router.put("/{item_id}", response_model=ItemRead)
async def update_item_endpoint(
        item_id: int,
        item_data: ItemUpdate,
        session: AsyncSession = Depends(get_session),
        current_user_id: int = Depends(get_current_user_id),
):
    item = await crud.get_item(session, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if item.owner_id != current_user_id:
        raise HTTPException(status_code=403, detail="Not authorized to update this item")

    updated_item = await crud.update_item(session, item_id, item_data)
    return updated_item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item_endpoint(
        item_id: int,
        session: AsyncSession = Depends(get_session),
        current_user_id: int = Depends(get_current_user_id),
):
    item = await crud.get_item(session, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if item.owner_id != current_user_id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this item")

    await crud.delete_item(session, item_id)
    return None
