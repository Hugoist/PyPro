import pytest
from bank_account import BankAccount
from unittest.mock import MagicMock


# Fixture to create a BankAccount instance
@pytest.fixture
def account():
    acc = BankAccount(100.0)  # start with 100
    return acc


# Parametrized test for deposits
@pytest.mark.parametrize("deposit_amount, expected_balance", [
    (50, 150),
    (0, 100),
    (200, 300)
])
def test_deposit(account, deposit_amount, expected_balance):
    account.deposit(deposit_amount)
    assert account.get_balance() == expected_balance


# Parametrized test for withdrawals
@pytest.mark.parametrize("withdraw_amount, expected_balance", [
    (50, 50),
    (0, 100),
    (100, 0)
])
def test_withdraw(account, withdraw_amount, expected_balance):
    if withdraw_amount > account.get_balance():
        with pytest.raises(ValueError):
            account.withdraw(withdraw_amount)
    else:
        account.withdraw(withdraw_amount)
        assert account.get_balance() == expected_balance


# Skip test if account balance is zero
@pytest.mark.skipif(BankAccount(0).get_balance() == 0, reason="Account is empty")
def test_withdraw_skip(account):
    account.withdraw(50)
    assert account.get_balance() == 50


# Test negative deposit and withdrawal
def test_negative_deposit(account):
    with pytest.raises(ValueError):
        account.deposit(-10)


def test_negative_withdraw(account):
    with pytest.raises(ValueError):
        account.withdraw(-20)


# Mock example for external API interaction (simulated)
def test_mock_external_api(monkeypatch):
    mock_api = MagicMock()
    mock_api.get_balance.return_value = 99.0

    # Suppose our BankAccount interacts with this API
    account = BankAccount()
    account.get_balance = mock_api.get_balance

    assert account.get_balance() == 99.0
    mock_api.get_balance.assert_called_once()
