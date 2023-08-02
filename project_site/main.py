from fastapi import FastAPI
from user import users

app=FastAPI()
app.include_router(users.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}



