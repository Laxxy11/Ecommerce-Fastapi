from uuid import UUID

import edgedb
from carts.route.views import cart_list, create_cart, delete_cart
from carts.schemas import Cart
from fastapi import APIRouter, Depends, status
from utils.response import success_response

from project_site.auth.Dependency import get_current_user

router = APIRouter(tags=["Cart"])
client = edgedb.create_async_client()


@router.get("/carts/", status_code=status.HTTP_200_OK)
async def get_cart(user=Depends(get_current_user)):
    """Api endpoint for reading all the categories"""
    data = await cart_list(client, user_id=user.id)
    return await success_response(
        status_code=200,
        msg="Successfully Reterived Data",
        data_info=data,
    )


@router.post("/cart/create/", status_code=status.HTTP_201_CREATED)
async def create_new_cart(cart: Cart.CartCreate, user=Depends(get_current_user)):
    data = await create_cart(client, cart, user_id=user.id)
    return await success_response(
        status_code=201,
        data_info=data,
        msg="Successfully Created",
    )


@router.delete("/cart/delete/{cart_id}", status_code=status.HTTP_200_OK)
async def remove_product(cart_id: UUID, user=Depends(get_current_user)):
    data = await delete_cart(client, cart_id, user_id=user.id)
    return await success_response(
        status_code=200,
        data_info=data,
        msg="Successfully deleted",
    )


# @router.put("/products/{product_id}", status_code=status.HTTP_200_OK)
# async def update_product(
#     product_id: UUID, request: product_schema.Product, user=Depends(get_current_user)
# ):
#     data = await db_product_update(client, product_id, request, user_id=user.id)
#     return await success_response(
#         status_code=200, data_info=data, msg="successfully updated"
#     )
