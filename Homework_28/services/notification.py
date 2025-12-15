class Notification:
    def register(self, event_bus):
        event_bus.subscribe("order.created", self.send_email)
        event_bus.subscribe("order.paid", self.send_sms)

    def send_email(self, data):
        print("EMAIL SENT:", data)

    def send_sms(self, data):
        print("SMS SENT:", data)
