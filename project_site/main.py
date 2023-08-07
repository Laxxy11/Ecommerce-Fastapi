from auth.route import authentication
from fastapi import FastAPI

from project_site.carts.route import carts
from project_site.product.route import category, products
from project_site.user.route import users

app = FastAPI()
app.include_router(authentication.router)
app.include_router(users.router)
app.include_router(category.router)
app.include_router(products.router)
app.include_router(carts.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
