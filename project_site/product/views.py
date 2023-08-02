from fastapi import HTTPException, status
from product.queries import (
    create_category_async_edgeql,
    get_category_async_edgeql,
    get_category_by_name_async_edgeql,
)


async def category_list(session):
    db_category = await get_category_async_edgeql.get_category(session)
    return db_category


async def category_by_name(session, category):
    db_category = await get_category_by_name_async_edgeql.get_category_by_name(
        session, name=category
    )
    if not db_category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": f"Category '{category}' does not exist."},
        )
    return db_category


async def create_category(session, category):
    db_category = await get_category_by_name_async_edgeql.get_category_by_name(
        session, name=category
    )
    if db_category:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Category already exist",
        )
    db_category = await create_category_async_edgeql.create_category(
        session, name=category
    )
    return db_category
