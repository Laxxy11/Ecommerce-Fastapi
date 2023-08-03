from fastapi import HTTPException, status
from product.queries import (
    create_category_async_edgeql,
    create_product_async_edgeql,
    delete_category_async_edgeql,
    delete_product_async_edgeql,
    get_category_async_edgeql,
    get_category_by_id_async_edgeql,
    get_category_by_name_async_edgeql,
    get_product_async_edgeql,
    get_product_by_id_async_edgeql,
    get_product_by_name_async_edgeql,
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


async def delete_category(session, category_id):
    db_category = await get_category_by_id_async_edgeql.get_category_by_id(
        session, category_id=category_id
    )
    if db_category is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No such Category exists",
        )
    db_category = await delete_category_async_edgeql.delete_category(
        session, category_id=category_id
    )
    return db_category


# for product--------------------------------------
async def product_list(session):
    db_products = await get_product_async_edgeql.get_product(session)
    return db_products


async def product_by_name(session, product):
    db_product = await get_product_by_name_async_edgeql.get_product_by_name(
        session, title=product
    )
    if not db_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": f"Product '{product}' does not exist."},
        )
    return db_product


async def create_product(session, product):
    db_product = await get_product_by_name_async_edgeql.get_product_by_name(
        session, title=product.title
    )
    if db_product:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Product already exist",
        )
    db_product = await create_product_async_edgeql.create_product(
        session,
        title=product.title,
        description=product.description,
        price=product.price,
        categories=product.categories,
    )
    return db_product


async def delete_product(session, product_id):
    db_product = await get_product_by_id_async_edgeql.get_product_by_id(
        session, product_id=product_id
    )
    if db_product is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No such Product exists",
        )
    db_product = await delete_product_async_edgeql.delete_product(
        session, id=product_id
    )
    return db_product
