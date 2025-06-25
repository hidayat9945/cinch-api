from sqlalchemy.orm import Session, joinedload
from app.db.models.products import Product

def get_product_by_id(db: Session, product_id: int):
    # Get a product by its ID
    product = db.query(Product).options(
        joinedload(Product.category),
        joinedload(Product.attribute_values).joinedload("attribute_value").joinedload("attribute"),
        joinedload(Product.pricings).joinedload("region"),
        joinedload(Product.pricings).joinedload("rental_period"),
    ).filter(Product.id == product_id).first()
    
    return product