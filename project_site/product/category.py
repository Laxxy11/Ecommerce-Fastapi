import edgedb
from fastapi import APIRouter, status
from product.views import category_by_name, category_list, create_category
from utils.response import success_response

router = APIRouter(tags=["Category"])
client = edgedb.create_async_client()


@router.get("/categories/", status_code=status.HTTP_200_OK)
async def get_categories():
    """Api endpoint for reading all the categories"""
    data = await category_list(client)
    return await success_response(
        status_code=200,
        msg="Successfully Reterived Data",
        data_info=data,
    )


@router.get("/categories/{category}", status_code=status.HTTP_200_OK)
async def get_category_by_name(category: str):
    """Api endpoint for reading categories"""
    data = await category_by_name(client, category)
    return await success_response(
        status_code=200,
        msg="Successfully Retrieved",
        data_info=data,
    )


@router.post("/categories", status_code=status.HTTP_201_CREATED)
async def create_new_category(category: str):
    data = await create_category(client, category)
    return await success_response(
        status_code=201,
        data_info=data,
        msg="Successfully Created",
    )
