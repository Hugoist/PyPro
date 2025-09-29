class InsufficientFundsException(Exception):
    """ Exception raised when insufficient funds """

    def __init__(
            self,
            required_amount: float,
            current_balance: float,
            currency: str = '',
            transaction_type: str = 'transaction'
    ) -> None:
        self.required_amount = required_amount
        self.current_balance = current_balance
        self.currency = currency
        self.transaction_type = transaction_type

        super().__init__(f"Insufficient funds for {transaction_type}: "
                         f"required {required_amount} {currency}, "
                         f"current balance {current_balance} {currency}")

    def pretty_message(self) -> str:
        return (f"Transaction failed!\n"
                f"Type: {self.transaction_type}\n"
                f"Required: {self.required_amount} {self.currency}\n"
                f"Available: {self.current_balance} {self.currency}")


class BankAccount:
    """
    Class representing a simple bank account
    """

    def __init__(self, initial_balance: float = 0.0):
        self._balance = initial_balance

    def deposit(self, amount: float) -> None:
        """
        Deposit money into the account
        """
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Withdraw money from the account
        """
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def get_balance(self) -> float:
        """
        Return the current account balance
        """
        return self._balance
