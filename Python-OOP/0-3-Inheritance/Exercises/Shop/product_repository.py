class ProductRepository:
    def __init__(self):
        self.products = []
    
    def add(self, product: object):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product
    
    def remove(self, product_name: str):
        product = self.find(product_name)
        if product is not None:
            self.products.remove(product)

    def __repr__(self):
        info = [f"{p.name}: {p.quantity}" for p in self.products]
        return '\n'.join(info)

