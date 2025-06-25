# init_db.py

from app.db.session import engine
from app.db.base import Base  # ini harus meng-import SEMUA model
from app.db.models.products import Product
from app.db.models.categories import Category
from app.db.models.attributes import Attribute
from app.db.models.attribute_values import AttributeValue
from app.db.models.product_attribute_values import ProductAttributeValue
from app.db.models.product_pricings import ProductPricing
from app.db.models.rental_periods import RentalPeriod
from app.db.models.regions import Region

def init():
    print("🔨 Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("✅ All tables created successfully!")

if __name__ == "__main__":
    init()
