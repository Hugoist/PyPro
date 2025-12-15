class Analytics:
    def __init__(self):
        self.orders_created = 0
        self.orders_paid = 0

    def register(self, event_bus):
        event_bus.subscribe("order.created", self.count_created)
        event_bus.subscribe("order.paid", self.count_paid)

    def count_created(self, data):
        self.orders_created += 1
        print("ORDERS CREATED:", self.orders_created)

    def count_paid(self, data):
        self.orders_paid += 1
        print("ORDERS PAID:", self.orders_paid)
