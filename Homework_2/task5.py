from typing import Callable

# Global list of events
events = []


def event_calendar() -> tuple[Callable[[str], None], Callable[[str], None], Callable[[], None]]:
    """Create event calendar"""

    # Adding a new event
    def add_event(event: str) -> None:
        events.append(event)
        print(f"Подія '{event}' додана.")

    # Removing an event
    def remove_event(event: str) -> None:
        if event in events:
            events.remove(event)
            print(f"Подія '{event}' видалена.")
        else:
            print(f"Подія '{event}' не знайдена.")

    # Showing all events
    def view_events() -> None:
        if events:
            print("Майбутні події:")
            for event_nmbr, event in enumerate(events, start=1):
                print(f"{event_nmbr}. {event}")
        else:
            print("Немає запланованих подій.")

    # Returning closures for further use
    return add_event, remove_event, view_events


add, remove, view = event_calendar()

add("Шикування")
add("Обід")
view()
remove("Шикування")
view()
