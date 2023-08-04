from carts.queries import (
    create_cart_async_edgeql,
    delete_cart_async_edgeql,
    get_cart_async_edgeql,
    get_cart_by_id_and_user_async_edgeql,
)
from fastapi import HTTPException, status
from product.queries import get_product_by_name_async_edgeql


async def cart_list(session, user_id):
    db_cart = await get_cart_async_edgeql.get_cart(session, user_id=user_id)
    return db_cart


async def create_cart(session, cart, user_id):
    db_product = await get_product_by_name_async_edgeql.get_product_by_name(
        session, title=cart.product
    )
    if db_product is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Such {cart.product} does not   exist",
        )
    db_cart = await create_cart_async_edgeql.create_cart(
        session, quantity=cart.quantity, title=cart.product, user_id=user_id
    )
    return db_cart


async def delete_cart(session, cart_id, user_id):
    db_cart = await get_cart_by_id_and_user_async_edgeql.get_cart_by_id_and_user(
        session, cart_id=cart_id, user_id=user_id
    )
    if db_cart is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No such Cart exists",
        )
    db_product = await delete_cart_async_edgeql.delete_cart(
        session, cart_id=cart_id, user_id=user_id
    )
    return db_product
