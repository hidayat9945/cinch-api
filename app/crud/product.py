from sqlalchemy.orm import Session, joinedload
from app.db.models.products import Product
from app.db.models.product_attribute_values import ProductAttributeValue
from app.db.models.attribute_values import AttributeValue
from app.db.models.product_pricings import ProductPricing

def get_product_by_id(db: Session, product_id: int):
    # Get a product by its ID
    product = db.query(Product).options(
        joinedload(Product.category),
        joinedload(Product.attribute_values).joinedload(ProductAttributeValue.attribute_value).joinedload(AttributeValue.attribute),
        joinedload(Product.pricings).joinedload(ProductPricing.region),
        joinedload(Product.pricings).joinedload(ProductPricing.rental_period),
    ).filter(Product.id == product_id).first()
    
    return product