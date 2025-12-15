from queue import Queue

from event_bus import EventBus
from event_worker import EventWorker
from services.analytics import Analytics
from services.notification import Notification
from services.order import Order


# =========================
# LEVEL 1 — EventBus check
# =========================

def l1_email_sender(data):
    print("L1 EMAIL:", data)


def l1_logger(data):
    print("L1 LOG:", data)


def l1_analytics(data):
    print("L1 ANALYTICS:", data)


bus = EventBus()

bus.subscribe("user.registered", l1_email_sender)
bus.subscribe("user.*", l1_logger)
bus.subscribe("order.created", l1_analytics)

bus.emit("user.registered", {"user_id": 1})
bus.emit("user.deleted", {"user_id": 1})
bus.emit("order.created", {"order_id": 101})

print("L1 EVENT LOG:", bus.get_event_log())

# =========================
# LEVEL 2 — Shop simulation
# =========================

event_queue = Queue()

worker = EventWorker(event_queue, bus)
worker.start()

notification = Notification()
notification.register(bus)

analytics_service = Analytics()
analytics_service.register(bus)

order_service = Order(event_queue)

order_service.create(1)
order_service.pay(1)
order_service.create(2)

event_queue.join()

print("FINAL EVENT LOG:", bus.get_event_log())
