from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        for item in self.products:
            if item.name == product_name:
                return item

    def remove(self, product_name):
        for item in self.products:
            if item.name == product_name:
                self.products.remove(item)

    def __repr__(self):
        information = ""
        for item in self.products:
            if self.products.index(item) == len(self.products) - 1:
                information += f"{item.name}: {item.quantity}"
                break
            information += f"{item.name}: {item.quantity}\n"
        return information
