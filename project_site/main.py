from fastapi import FastAPI
from product import category, products
from user import users

app = FastAPI()
app.include_router(users.router)
app.include_router(category.router)
app.include_router(products.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
