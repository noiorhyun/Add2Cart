from models import Product

# --- Catalog Data ---
RAW_PRODUCTS = [
    {"id": 101, "name": "Laptop Pro X", "price": 1200.00, "rating": 4.8},
    {"id": 102, "name": "Mechanical Keyboard", "price": 85.50, "rating": 4.5},
    {"id": 103, "name": "Wireless Mouse", "price": 25.99, "rating": 4.1},
    {"id": 104, "name": "4K Monitor 27in", "price": 350.00, "rating": 4.7},
    {"id": 105, "name": "USB-C Hub", "price": 15.00, "rating": 3.9},
    {"id": 106, "name": "Gaming Headset", "price": 75.99, "rating": 4.6},
    {"id": 107, "name": "Webcam HD", "price": 30.50, "rating": 4.0},
    {"id": 108, "name": "SSD 1TB Portable", "price": 95.00, "rating": 4.9},
    {"id": 109, "name": "LED Desk Lamp", "price": 40.00, "rating": 4.2},
    {"id": 110, "name": "Ergonomic Chair", "price": 450.00, "rating": 4.3},
    {"id": 111, "name": "Smartphone Charger", "price": 18.99, "rating": 3.5},
    {"id": 112, "name": "Noise Cancelling Earbuds", "price": 150.00, "rating": 4.4},
]

# --- Initial Setup ---

# List of Product objects (O(n) for iteration/sorting)
PRODUCT_CATALOG = [Product(**p) for p in RAW_PRODUCTS]

# Hash Table for O(1) lookup by ID
# NOTE: IDs are stored as strings to match the Product object's ID
PRODUCTS_BY_ID = {p.id: p for p in PRODUCT_CATALOG}
