import uuid
from datetime import datetime

class Product:
    """Represents a single product in the catalog."""
    def __init__(self, product_id, name, price, rating):
        self.id = str(product_id)
        self.name = name
        self.price = price  # Used for sorting (ascending)
        self.rating = rating  # Used for sorting (descending)
    
    def __repr__(self):
        return f"Product(ID:{self.id}, Name:'{self.name}', Price:${self.price:.2f}, Rating:{self.rating})"

class Order:
    """Represents a submitted order ready for processing."""
    def __init__(self, items, total_cost):
        self.order_id = str(uuid.uuid4())[:8].upper() # Generate a short unique ID
        self.items = items
        self.total_cost = total_cost
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __repr__(self):
        return (f"Order(ID:{self.order_id}, Total:${self.total_cost:.2f}, "
                f"Items:{len(self.items)} distinct products, Time:{self.timestamp})")
    