default_time: int = 60


def training_session(rounds: int) -> None:
    """Create training session"""

    time_per_round = default_time

    # Modify training session time round by round
    def adjust_time() -> None:
        nonlocal time_per_round
        round_time_adjustment = 5
        time_per_round -= round_time_adjustment

    print("Результат")

    # Loop through each round (from 1 to 'rounds' inclusive)
    for round_nmbr in range(1, rounds + 1):
        if round_nmbr == 1:
            # For the first round, show the default time
            print(f"Раунд {round_nmbr}: {time_per_round} хвилин")
        else:
            # For the next rounds, show the adjusted time
            adjust_time()
            print(f"Раунд {round_nmbr}: {time_per_round} хвилин (після коригування часу)")


# Результат
# Раунд 1: 60 хвилин
# Раунд 3: 60 хвилин (після коригування часу)
# Раунд 2: 60 хвилин (після коригування часу)
training_session(3)
