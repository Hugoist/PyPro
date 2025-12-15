class Order:
    def __init__(self, event_queue):
        self.queue = event_queue

    def create(self, order_id):
        self.queue.put(("order.created", {"order_id": order_id}))

    def pay(self, order_id):
        self.queue.put(("order.paid", {"order_id": order_id}))
