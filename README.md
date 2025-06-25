# Cinch Take-Home Project – Product API
## OVERVIEW
A FastAPI backend for managing products, categories, attributes, and pricing — designed with clean architecture and relational data.

## TECH STACK
Followings are the tech stack used in this project:
- Python 3.10+
- FastAPI – Web framework
- SQLAlchemy – ORM & relational modeling
- Pydantic – Data validation & serialization
- SQLite – Local development database
- Uvicorn – ASGI server for running the app

## PROJECT STRUCTURE
As we want to design a clean and scalable architecture, we will use the following structure:

```
app/
├── api/                # Route handlers (e.g., product endpoints)
├── crud/               # DB access logic
├── db/
│   ├── base.py         # Imports all models for table creation
│   ├── base_class.py   # Declarative Base class
│   ├── session.py      # DB engine & session maker
│   ├── timestamp_mixin.py
│   └── models/         # SQLAlchemy models (product, category, etc.)
├── schemas/            # Pydantic schemas for request & response
└── main.py             # FastAPI app entry point
requirements.txt
```

## SETUP
To set up the project, follow these steps:
1. Install dependencies
    
    It is recommended to use a virtual environment. You can create one using the following command:
    ```bash
    python -m venv venv
    source venv/bin/activate 
    pip install -r requirements.txt
    ```

2. Initialize database
    
    ```bash
    python init_db.py
    ```

3. Seed dummy data

    ```bash
    python seed_dummy.py
    ```

4. Run the server

    ```bash
    uvicorn app.main:app --reload
    ```

    Open your browser and navigate to `http://localhost:8000/docs` to see the API documentation.

## EXAMPLE RESPONSE

### Get product by id

```json
{
    "id": 1,
    "name": "Smartphone",
    "description": null,
    "sku": "SKU123",
    "category": {
        "id": 1,
        "name": "Electronics"
    },
    "attribute_values": [
        {
        "attribute_value": {
            "id": 1,
            "value": "Red",
            "attribute": {
            "id": 1,
            "name": "Color"
            }
        }
        },
        {
        "attribute_value": {
            "id": 2,
            "value": "Blue",
            "attribute": {
            "id": 1,
            "name": "Color"
            }
        }
        }
    ],
    "pricings": [
        {
        "id": 1,
        "region": {
            "id": 1,
            "name": "Jakarta"
        },
        "rental_period": {
            "id": 1,
            "duration_months": 3
        },
        "price": 150000
        }
    ]
}
```

### No data found
```json
{
  "detail": "Product not found"
}
```