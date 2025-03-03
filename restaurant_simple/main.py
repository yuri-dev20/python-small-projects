from product import Product
from order_status import OrderStatus
from order_item import OrderItem
from order import Order
from client import Client
import datetime


def main():
    print("Enter cliente data:")
    cli_name = str(input("Name: "))
    cli_email = str(input("Email: "))
    client = Client(cli_name, cli_email)
    print()

    print("Enter order data:")
    print("STATUS: " + OrderStatus.PROCESSING.value)
    orders = int(input("How many items to this order?: "))

    order = Order(datetime.datetime.now(), client)
    for i in range(orders):
        print()
        print(f"Enter the #{i+1} item data:")
        prod_name = str(input("Product name: "))
        prod_price = float(input("Product price: "))
        quantity = int(input("Quantity: "))

        prod = Product(prod_name, prod_price)
        order_item = OrderItem(quantity, prod_price, prod)
        order.addItem(order_item)

    print()
    order.order_summary()


if __name__ == '__main__':
    main()
