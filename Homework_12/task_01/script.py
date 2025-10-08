from datetime import datetime, timedelta
from pymongo import MongoClient

# connect to DB
client = MongoClient("mongodb://localhost:27017/shop")
shopDB = client.get_database()
products = shopDB.products
orders = shopDB.orders

# Add several products
if products is not None:
    shopDB.products.insert_many([
        {"name": "Keyboard", "price": 199.00, "quantity": 5, "category": "Accessories"},
        {"name": "Black tea", "price": 20.00, "quantity": 8, "category": "Groceries"},
    ])

# Get recent orders
thirty_days_ago = datetime.now() - timedelta(days=30)
recent_orders = list(orders.find({"order_date": {"$gte": thirty_days_ago}}))
print("\nOrders from last 30 days:")
for order in recent_orders:
    print(order)

# Update products quantity
if recent_orders:
    for order in recent_orders:
        for item in order["items"]:
            print(products.find_one({"name": item["name"]}, {"_id": 0, "name": 1, "quantity": 1}))
            products.update_one(
                {"name": item["name"]},
                {"$inc": {"quantity": -item["quantity"]}}
            )
            print(products.find_one({"name": item["name"]}, {"_id": 0, "name": 1, "quantity": 1}))
        print("\n Product quantities updated")

# Remove unavailable products
result = products.delete_many({"quantity": 0})
print(f"{result.deleted_count} product(s) removed")
