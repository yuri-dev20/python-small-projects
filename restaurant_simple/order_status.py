from enum import Enum


class OrderStatus(Enum):
    PENDING_PAYMENT = "Pending Payment"
    PROCESSING = "Processing"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"
