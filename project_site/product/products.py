from uuid import UUID

import edgedb
from fastapi import APIRouter, status
from product.schemas import product_schema
from product.views import (
    create_product,
    db_product_update,
    delete_product,
    product_by_name,
    product_list,
)
from utils.response import success_response

router = APIRouter(tags=["Product"])
client = edgedb.create_async_client()


@router.get("/products/", status_code=status.HTTP_200_OK)
async def get_products():
    """Api endpoint for reading all the categories"""
    data = await product_list(client)
    return await success_response(
        status_code=200,
        msg="Successfully Reterived Data",
        data_info=data,
    )


@router.get("/products/{product}/", status_code=status.HTTP_200_OK)
async def get_product_by_name(product: str):
    """Api endpoint for reading categories"""
    data = await product_by_name(client, product)
    return await success_response(
        status_code=200,
        msg="Successfully Retrieved",
        data_info=data,
    )


@router.post("/products/", status_code=status.HTTP_201_CREATED)
async def create_new_product(product: product_schema.Product):
    data = await create_product(client, product)
    return await success_response(
        status_code=201,
        data_info=data,
        msg="Successfully Created",
    )


@router.delete("/products/{product_id}", status_code=status.HTTP_200_OK)
async def remove_product(product_id: UUID):
    data = await delete_product(client, product_id)
    return await success_response(
        status_code=200,
        data_info=data,
        msg="Successfully deleted",
    )


@router.put("/products/{product_id}", status_code=status.HTTP_200_OK)
async def update_product(product_id: UUID, request: product_schema.Product):
    data = await db_product_update(client, product_id, request)
    return await success_response(
        status_code=200, data_info=data, msg="successfully updated"
    )
