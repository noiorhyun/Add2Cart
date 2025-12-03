class Product:
    def __init__(self, id, name, price, rating):
        self.id = id
        self.name = name
        self.price = price
        self.rating = rating
    
    def __repr__(self):
        return f"{self.id} | {self.name} | ${self.price:.2f} | ⭐ {self.rating}"
