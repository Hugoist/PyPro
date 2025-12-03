from ninja import Router
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.db import transaction

from app.api.auth import auth
from app.models.ecommerce import Product, Cart, CartItem, Order, OrderItem
from app.schemas.ecommerce import (
    ProductCreateSchema, ProductUpdateSchema, ProductReadSchema,
    CartItemAddSchema, CartReadSchema, CartItemReadSchema,
    OrderCreateSchema, OrderReadSchema, OrderItemReadSchema, OrderUpdateSchema
)

router = Router(tags=["Ecommerce"])


# PRODUCT CRUD

@router.post("/products", auth=auth, response=ProductReadSchema)
def create_product(request, data: ProductCreateSchema):
    product = Product.objects.create(**data.dict())
    return product


@router.get("/products", response=list[ProductReadSchema])
def list_products(request):
    return Product.objects.all()


@router.get("/products/{product_id}", response=ProductReadSchema)
def get_product(request, product_id: int):
    return get_object_or_404(Product, id=product_id)


@router.put("/products/{product_id}", auth=auth, response=ProductReadSchema)
def update_product(request, product_id: int, data: ProductUpdateSchema):
    product = get_object_or_404(Product, id=product_id)

    for field, value in data.dict(exclude_unset=True).items():
        setattr(product, field, value)

    product.save()
    return product


@router.delete("/products/{product_id}", auth=auth)
def delete_product(request, product_id: int):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return {"success": True}


# CART

def get_or_create_cart(user: User) -> Cart:
    cart, _ = Cart.objects.get_or_create(user=user, is_active=True)
    return cart


@router.post("/cart/add", auth=auth, response=CartReadSchema)
def cart_add_item(request, data: CartItemAddSchema):
    cart = get_or_create_cart(request.user)
    product = get_object_or_404(Product, id=data.product_id)

    item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if created:
        item.quantity = data.quantity
    else:
        item.quantity += data.quantity

    item.save()

    return cart.to_schema()


@router.get("/cart", auth=auth, response=CartReadSchema)
def get_cart(request):
    cart = get_or_create_cart(request.user)
    return cart.to_schema()


@router.delete("/cart/item/{item_id}", auth=auth, response=CartReadSchema)
def remove_cart_item(request, item_id: int):
    cart = get_or_create_cart(request.user)
    item = get_object_or_404(CartItem, id=item_id, cart=cart)

    item.delete()
    return cart.to_schema()


# ORDER

@router.post("/orders", auth=auth, response=OrderReadSchema)
def create_order(request, data: OrderCreateSchema):
    cart = get_object_or_404(Cart, id=data.cart_id, user=request.user, is_active=True)

    if cart.items.count() == 0:
        return {"error": "Cart is empty"}

    with transaction.atomic():
        order = Order.objects.create(user=request.user, total_price=cart.total_price)

        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.quantity * item.product.price
            )

        # deactivate cart
        cart.is_active = False
        cart.save()

    return order.to_schema()


@router.get("/orders", auth=auth, response=list[OrderReadSchema])
def list_orders(request):
    return [order.to_schema() for order in Order.objects.filter(user=request.user)]


@router.get("/orders/{order_id}", auth=auth, response=OrderReadSchema)
def get_order(request, order_id: int):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return order.to_schema()


@router.put("/orders/{order_id}", auth=auth, response=OrderReadSchema)
def update_order_status(request, order_id: int, data: OrderUpdateSchema):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    order.status = data.status
    order.save()

    return order.to_schema()
