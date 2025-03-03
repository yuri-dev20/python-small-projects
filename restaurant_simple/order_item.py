from product import Product


class OrderItem:
    def __init__(self, quantity: int, price: float, product: Product) -> None:
        self.quantity = quantity
        self.price = product.price
        self.product = product

    def subTotal(self):
        return self.price * self.quantity
