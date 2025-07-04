from fastapi import APIRouter
from app.api.v1 import product

api_router = APIRouter()
api_router.include_router(product.router)