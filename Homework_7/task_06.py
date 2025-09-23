from abc import ABC, abstractmethod
import random


class MessageSender(ABC):
    """
    Target interface for sending messages
    """

    @abstractmethod
    def send_message(self, message: str) -> None:
        """
        Send a message
        """
        pass


class SMSService:
    """
    Adaptee: service for sending SMS messages.
    """

    def send_sms(self, phone_number: str, message: str) -> None:
        # Simulate sending with possible failure
        if random.choice([True, False]):
            raise ConnectionError("SMS gateway unreachable")
        print(f"SMS to {phone_number}: {message}")


class EmailService:
    """
    Adaptee: service for sending Email messages.
    """

    def send_email(self, email_address: str, message: str) -> None:
        # Simulate sending with possible failure
        if random.choice([True, False]):
            raise TimeoutError("Email server did not respond")
        print(f"Email to {email_address}: {message}")


class PushService:
    """
    Adaptee: service for sending Push notifications.
    """

    def send_push(self, device_id: str, message: str) -> None:
        # Simulate sending with possible failure
        if random.choice([True, False]):
            raise RuntimeError("Push service error")
        print(f"Push notification to {device_id}: {message}")


class SMSAdapter(MessageSender):
    """
    Adapter for SMSService to fit MessageSender interface.
    """

    def __init__(self, service: SMSService, phone_number: str):
        self.service = service
        self.phone_number = phone_number

    def send_message(self, message: str) -> None:
        self.service.send_sms(self.phone_number, message)


class EmailAdapter(MessageSender):
    """
    Adapter for EmailService to fit MessageSender interface.
    """

    def __init__(self, service: EmailService, email_address: str):
        self.service = service
        self.email_address = email_address

    def send_message(self, message: str) -> None:
        self.service.send_email(self.email_address, message)


class PushAdapter(MessageSender):
    """
    Adapter for PushService to fit MessageSender interface.
    """

    def __init__(self, service: PushService, device_id: str):
        self.service = service
        self.device_id = device_id

    def send_message(self, message: str) -> None:
        self.service.send_push(self.device_id, message)


class MessageSystem:
    """
    System for sending messages through multiple adapters.
    """

    def __init__(self, senders: list[MessageSender]):
        self.senders = senders

    def broadcast(self, message: str) -> None:
        """
        Send the same message through all available services.

        Args:
            message (str): Message content.

        Returns:
            None
        """
        for sender in self.senders:
            try:
                sender.send_message(message)
            except Exception as e:
                print(f"[ERROR] Failed to send via {sender.__class__.__name__}: {e}")


# Tests
message = "Hello, world!"

sms_sender = SMSAdapter(SMSService(), "+380501234567")
email_sender = EmailAdapter(EmailService(), "user@example.com")
push_sender = PushAdapter(PushService(), "device123")

system = MessageSystem([sms_sender, email_sender, push_sender])
system.broadcast(message)
