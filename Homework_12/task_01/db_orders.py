from datetime import datetime

# Seeds for Orders collection
orders = [
    {
        "order_number": 1001,
        "order_date": datetime.strptime("2025-09-03", "%Y-%m-%d"),
        "client_id": 1,
        "items": [
            {"name": "Laptop Lenovo IdeaPad", "quantity": 1, "price": 18999.99},
            {"name": "Wireless Mouse Logitech M185", "quantity": 1, "price": 599}
        ],
        "total_price": 19598.99
    },
    {
        "order_number": 1002,
        "order_date": datetime.strptime("2025-09-06", "%Y-%m-%d"),
        "client_id": 2,
        "items": [
            {"name": "Smartphone Samsung Galaxy A55", "quantity": 1, "price": 18499},
            {"name": "USB-C Cable 1m", "quantity": 2, "price": 199.99}
        ],
        "total_price": 18898.98
    },
    {
        "order_number": 1003,
        "order_date": datetime.strptime("2025-09-10", "%Y-%m-%d"),
        "client_id": 3,
        "items": [
            {"name": "Coffee Arabica Premium", "quantity": 3, "price": 320.5},
            {"name": "Notebook A5 Classic", "quantity": 2, "price": 79.5}
        ],
        "total_price": 1120.5
    },
    {
        "order_number": 1004,
        "order_date": datetime.strptime("2025-09-15", "%Y-%m-%d"),
        "client_id": 4,
        "items": [
            {"name": "Running Shoes Nike Air Zoom", "quantity": 1, "price": 3599},
            {"name": "Backpack UrbanPro 25L", "quantity": 1, "price": 1150.75}
        ],
        "total_price": 4749.75
    },
    {
        "order_number": 1005,
        "order_date": datetime.strptime("2025-09-19", "%Y-%m-%d"),
        "client_id": 5,
        "items": [
            {"name": "LED Desk Lamp", "quantity": 1, "price": 720},
            {"name": "Bluetooth Speaker JBL Go 3", "quantity": 1, "price": 1599}
        ],
        "total_price": 2319.0
    },
    {
        "order_number": 1006,
        "order_date": datetime.strptime("2025-09-23", "%Y-%m-%d"),
        "client_id": 6,
        "items": [
            {"name": "Smartphone Samsung Galaxy A55", "quantity": 1, "price": 18499},
            {"name": "Bluetooth Speaker JBL Go 3", "quantity": 1, "price": 1599}
        ],
        "total_price": 20098.0
    },
    {
        "order_number": 1007,
        "order_date": datetime.strptime("2025-09-27", "%Y-%m-%d"),
        "client_id": 2,
        "items": [
            {"name": "USB-C Cable 1m", "quantity": 3, "price": 199.99},
            {"name": "Notebook A5 Classic", "quantity": 5, "price": 79.5}
        ],
        "total_price": 1158.47
    },
    {
        "order_number": 1008,
        "order_date": datetime.strptime("2025-09-30", "%Y-%m-%d"),
        "client_id": 3,
        "items": [
            {"name": "Laptop Lenovo IdeaPad", "quantity": 1, "price": 18999.99}
        ],
        "total_price": 18999.99
    },
    {
        "order_number": 1009,
        "order_date": datetime.strptime("2025-10-03", "%Y-%m-%d"),
        "client_id": 4,
        "items": [
            {"name": "Running Shoes Nike Air Zoom", "quantity": 2, "price": 3599},
            {"name": "Backpack UrbanPro 25L", "quantity": 1, "price": 1150.75}
        ],
        "total_price": 8348.75
    },
    {
        "order_number": 1010,
        "order_date": datetime.strptime("2025-10-06", "%Y-%m-%d"),
        "client_id": 5,
        "items": [
            {"name": "Coffee Arabica Premium", "quantity": 2, "price": 320.5},
            {"name": "LED Desk Lamp", "quantity": 1, "price": 720}
        ],
        "total_price": 1361.0
    }
]
