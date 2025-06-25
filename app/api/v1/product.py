from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud.product import get_product_by_id
from app.schemas.product import ProductSchema
from app.api.deps import get_db

router = APIRouter(prefix="/products")

@router.get("/{product_id}", response_model=ProductSchema)
def get_product(product_id: int, db: Session = Depends(get_db)):
    # Get a product by its ID
    product = get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    return product