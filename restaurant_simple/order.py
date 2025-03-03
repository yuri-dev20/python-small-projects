import datetime
from order_status import OrderStatus
from order_item import OrderItem
from client import Client


class Order:
    def __init__(self, moment: datetime, client: Client) -> None:
        self.moment = moment
        self.order_item = []
        self.client = client

    def addItem(self, item: OrderItem) -> None:
        self.order_item.append(item)

    def removeItem(self, item: OrderItem) -> None:
        self.order_item.remove(item)

    def total(self) -> float:
        total = 0
        for items in self.order_item:
            total += items.subTotal()

        return total

    def order_summary(self):
        print('---------------------------------------')
        print(f"Order Summary: \nOrder moment: {self.moment.strftime("%Y-%m-%d %H:%M:%S")} \nOrder status: {
              OrderStatus.PROCESSING.value} \nClient: {self.client.name} -\n {self.client.email} \n")

        print(f"Order Items: \n")

        for item in self.order_item:
            print(f"{item.product.name}, ${item.product.price:.2f}, Quantity: {
                  item.quantity}, Subtotal: ${item.subTotal():.2f}")
        print(f"Total price: {self.total():.2f}")
