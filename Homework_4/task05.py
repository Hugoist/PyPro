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
    """Class representing a bank account"""

    def __init__(self, balance: float, currency: str = "UAH") -> None:
        self.balance = balance
        self.currency = currency

    # charge balance
    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            raise InsufficientFundsException(
                required_amount=amount,
                current_balance=self.balance,
                currency=self.currency,
                transaction_type="withdrawal"
            )
        self.balance -= amount
        self.__succesful_transaction()

    # make deposit
    def deposit(self, amount: float) -> None:
        if amount > self.balance:
            raise InsufficientFundsException(
                required_amount=amount,
                current_balance=self.balance,
                currency=self.currency,
                transaction_type="purchase"
            )
        self.balance += amount
        self.__succesful_transaction()

    # inform after succesful transaction
    def __succesful_transaction(self) -> None:
        print(f"Transaction successful. Available balance: {self.balance} {self.currency}")

    def __repr__(self) -> str:
        return f"Bank account balance: {self.balance} {self.currency}\n"


account = BankAccount(balance=100, currency="EUR")

print(account)  # Bank account balance: 100 EUR

try:
    account.deposit(50)  # Transaction successful. Available balance: 150 EUR
    print(account)  # Bank account balance: 150 EUR

    # Transaction failed!
    # Type: withdrawal
    # Required: 180 EUR
    # Available: 150 EUR
    account.withdraw(180)
except InsufficientFundsException as e:
    print(e.pretty_message())

print(account)  # Bank account balance: 50 EUR
