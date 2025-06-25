# seed_dummy_data.py

from app.db.session import SessionLocal
from app.db.models.products import Product
from app.db.models.categories import Category
from app.db.models.attributes import Attribute
from app.db.models.attribute_values import AttributeValue
from app.db.models.product_attribute_values import ProductAttributeValue
from app.db.models.product_pricings import ProductPricing
from app.db.models.regions import Region
from app.db.models.rental_periods import RentalPeriod

def seed():
    db = SessionLocal()

    # Create category
    electronics = Category(name="Electronics")
    db.add(electronics)
    db.flush()  # get id

    # Create product
    phone = Product(name="Smartphone", category_id=electronics.id, sku="SKU123")
    db.add(phone)
    db.flush()

    # Create attribute
    color_attr = Attribute(name="Color")
    db.add(color_attr)
    db.flush()

    # Create attribute value
    red = AttributeValue(value="Red", attribute_id=color_attr.id)
    blue = AttributeValue(value="Blue", attribute_id=color_attr.id)
    db.add_all([red, blue])
    db.flush()

    # Relate product <-> attribute value
    pav1 = ProductAttributeValue(product_id=phone.id, attribute_value_id=red.id)
    pav2 = ProductAttributeValue(product_id=phone.id, attribute_value_id=blue.id)
    db.add_all([pav1, pav2])

    # Region
    jakarta = Region(name="Jakarta")
    db.add(jakarta)
    db.flush()

    # Rental period
    three = RentalPeriod(duration_months=3)
    db.add(three)
    six = RentalPeriod(duration_months=6)
    db.add(six)
    twelve = RentalPeriod(duration_months=12)
    db.add(twelve)
    db.flush()

    # Product pricing
    pricing = ProductPricing(product_id=phone.id, region_id=jakarta.id, rental_period_id=three.id, price=150000)
    db.add(pricing)

    db.commit()
    db.close()
    print("✅ Dummy data inserted.")

if __name__ == "__main__":
    seed()
