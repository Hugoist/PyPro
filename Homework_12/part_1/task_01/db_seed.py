from db_orders import orders
from db_collections import collections
from db_products import products

from pymongo import MongoClient

# connect to DB
client = MongoClient("mongodb://localhost:27017/shop")
shopDB = client.get_database()

for collection in collections:
    # drop collection from database
    if collection["name"] in shopDB.list_collection_names():
        shopDB[collection["name"]].drop()

    # Create collection
    if collection["name"] not in shopDB.list_collection_names():
        shopDB.create_collection(
            collection["name"],
            validator=collection["validator"],
        )

# Seed Products collection
if 'products' in shopDB.list_collection_names():
    shopDB.products.insert_many(products)

# Seed Orders collection
if 'orders' in shopDB.list_collection_names():
    shopDB.orders.insert_many(orders)
