class Product:
    def __init__(self, id, name, price, rating):
        self.id = id
        self.name = name
        self.price = price
        self.rating = rating
    
    def __repr__(self):
        return f"{self.id} | {self.name} | ${self.price:.2f} | ⭐ {self.rating}"

class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items
        self.total_price = sum(p.price for p in items)

    def __repr__(self):
        item_names = ", ".join(p.name for p in self.items)
        return f"Order #{self.order_id}: {item_names} | Total: ${self.total_price:.2f}"
