import pytest
from user_manager import UserManager


@pytest.fixture
def user_manager():
    """
    Fixture that creates a UserManager with two users
    """
    um = UserManager()
    um.add_user("Liza", 33)
    um.add_user("Luka", 3)
    return um


def test_add_user(user_manager):
    """
    Test adding a new user increases the user list
    """
    user_manager.add_user("Alex", 35)
    all_users = user_manager.get_all_users()
    assert any(u["name"] == "Alex" for u in all_users)
    assert len(all_users) == 3


def test_remove_user(user_manager):
    """
    Test removing a user by name
    """
    user_manager.remove_user("Liza")
    all_users = user_manager.get_all_users()
    assert all(u["name"] != "I" for u in all_users)
    assert len(all_users) == 1


def test_get_all_users(user_manager):
    """
    Test getting all users returns the correct list
    """
    all_users = user_manager.get_all_users()
    names = [u["name"] for u in all_users]
    assert "Liza" in names
    assert "Luka" in names
    assert len(all_users) == 2


@pytest.mark.skipif(
    True,
    reason="Skip if user count is less than 3"
)
def test_skip_if_few_users(user_manager):
    """
    Test skipped if there are less than 3 users
    """
    assert len(user_manager.get_all_users()) >= 3
