from datetime import datetime
from typing import List
from typing import Literal

from ninja import Schema


# PRODUCT
class ProductCreateSchema(Schema):
    name: str
    price: float
    description: str | None = None
    stock: int = 0


class ProductUpdateSchema(Schema):
    name: str | None = None
    price: float | None = None
    description: str | None = None
    stock: int | None = None


class ProductReadSchema(Schema):
    id: int
    name: str
    description: str | None
    price: float
    stock: int
    created_at: datetime


# CART
class CartItemAddSchema(Schema):
    product_id: int
    quantity: int


class CartItemReadSchema(Schema):
    id: int
    product_id: int
    product_name: str
    quantity: int
    total_price: float


class CartReadSchema(Schema):
    items: List[CartItemReadSchema]
    total_price: float


# ORDER
class OrderItemReadSchema(Schema):
    product_id: int
    product_name: str
    quantity: int
    price: float


class OrderCreateSchema(Schema):
    cart_id: int


class OrderReadSchema(Schema):
    id: int
    status: str
    created_at: datetime
    items: List[OrderItemReadSchema]
    total_price: float


class OrderUpdateSchema(Schema):
    status: Literal["processing", "shipped", "delivered"]
