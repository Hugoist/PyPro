# config for shop Database
collections = [
    {
        "name": "products",
        "validator": {
            "$jsonSchema": {
                "bsonType": "object",
                "required": ["name", "price", "quantity", "category"],
                "properties": {
                    "name": {"bsonType": "string"},
                    "price": {
                        "bsonType": "double",
                        "minimum": 0,
                    },
                    "quantity": {
                        "bsonType": "int",
                        "minimum": 0,
                    },
                    "category": {"bsonType": "string"}
                },
            }
        },
    },
    {
        "name": "orders",
        "validator": {
            "$jsonSchema": {
                "bsonType": "object",
                "required": ["order_number", "order_date", "client_id", "items", "total_price"],
                "properties": {
                    "order_number": {
                        "bsonType": "int",
                        "minimum": 1
                    },
                    "order_date": {
                        "bsonType": "date",
                    },
                    "client_id": {
                        "bsonType": "int",
                        "minimum": 1
                    },
                    "items": {
                        "bsonType": "array",
                        "properties": {
                            "name": {"bsonType": "string"},
                            "quantity": {
                                "bsonType": "int",
                                "minimum": 1,
                            },
                            "price": {
                                "bsonType": "double",
                                "minimum": 0,
                            }
                        }
                    },
                    "total_price": {
                        "bsonType": "double",
                        "minimum": 0,
                    }
                }
            }
        }
    }
]
