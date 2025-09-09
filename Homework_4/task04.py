class InsufficientResourcesException(Exception):
    """Exception raised when a player doesn't have enough resources for an action"""

    def __init__(self, required_resource: str, required_amount: float, current_amount: float):
        self.required_resource = required_resource
        self.required_amount = required_amount
        self.current_amount = current_amount
        super().__init__(f"Not enough {required_resource}: required {required_amount}, current {current_amount}")


class Player:
    """ Class representing a player """

    def __init__(self, gold: float, mana: float):
        self.gold = gold
        self.mana = mana

    def spend_resource(self, resource_type: str, amount: float):
        # check if attribute exists
        if not hasattr(self, resource_type):
            raise AttributeError(f"Unknown resource: {resource_type}")

        current_amount = getattr(self, resource_type)
        if amount > current_amount:
            raise InsufficientResourcesException(
                required_resource=resource_type,
                required_amount=amount,
                current_amount=current_amount
            )

        # set new resource amount after spending
        setattr(self, resource_type, current_amount - amount)
        print(f"Spend {resource_type}: -{amount}")

    def __repr__(self) -> str:
        return f"Player has {self.gold} gold and {self.mana} mana"


player = Player(gold=100, mana=50)

try:
    print(player)  # Player has 100 gold and 50 mana
    player.spend_resource("gold", 30)  # Spend gold: -30
    print(player)  # Player has 70 gold and 50 mana
    player.spend_resource("mana", 60)
except InsufficientResourcesException as e:
    print(e)  # Not enough mana: required 60, current 50
    print(player)  # Player has 70 gold and 50 mana
