from fastapi import FastAPI
from app.routers import category, product, service

app = FastAPI()

app.include_router(category.router)
app.include_router(product.router)
app.include_router(service.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the CRUD API!"}