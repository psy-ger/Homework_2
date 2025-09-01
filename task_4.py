
default_time: int = 60  # default time in minutes


def training_session(rounds: int) -> None:
    """function to manage training session rounds with adjustable time"""
    for i in range(1, rounds+1):
        time_per_round: int = default_time   # default time per round
        print(
            f"Час на раунд за замовчуванням: {time_per_round} хвилин {i} раунд")

        def adjust_time(new_time: int) -> None:
            """function to adjust time per round"""
            nonlocal time_per_round
            time_per_round = new_time  # adjust time for the round
        if i == 2:
            adjust_time(55)
        if i == 3:
            adjust_time(50)
        print(f"Раунд {i}: {time_per_round} хвилин")


training_session(3)
