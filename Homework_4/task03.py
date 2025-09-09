class GameEventException(Exception):
    """Custom exception for game events with detailed informatio."""

    def __init__(self, type: str, details: dict):
        self.type = type
        self.details = details
        super().__init__(f"Game event {type} is happen")

    # prettify event details
    def pretty_details(self) -> str:
        lines = [f"\t{key}: {value}" for key, value in self.details.items()]
        return "\n".join(lines)


events = [
    {"type": "death", "details": {"cause": "sword strike"}},
    {"type": "death", "details": {"cause": "falling"}},
    {"type": "levelUp", "details": {"new_level": 5, "xp_gained": 1500}},
]

for event in events:
    try:
        raise GameEventException(event["type"], event["details"])
    except GameEventException as gee:
        print(f"\nEvent caught: {gee.type}")
        print("Details:")
        print(gee.pretty_details())
