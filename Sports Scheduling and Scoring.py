
def sports_scheduling_and_scoring():
    events = [
        ("Football", "Falcons", "Monday", 10, 12, 3),
        ("Basketball", "Falcons", "Monday", 11, 13, 2),
        ("Tennis", "Tigers", "Monday", 10, 11, 3),
        ("Volleyball", "Tigers", "Tuesday", 14, 16, 1),
        ("Cricket", "Falcons", "Wednesday", 9, 12, 3),
        ("Swimming", "Sharks", "Tuesday", 10, 11, 3),
        ("Athletics", "Sharks", "Wednesday", 9, 10, 2),
    ]

    print("Schedule:")
    for event in events:
        print(event)

    print("\nScheduling conflicts:")
    for i, a in enumerate(events):
        for b in events[i + 1:]:
            same_team_day = a[1] == b[1] and a[2] == b[2]
            overlap = max(a[3], b[3]) < min(a[4], b[4])

            if same_team_day and overlap:
                print(a[1], ":", a[0], "overlaps with", b[0])

    scores = {}
    for event, team, day, start, end, points in events:
        scores[team] = scores.get(team, 0) + points

    rankings = sorted(scores.items(),
                      key=lambda item: (-item[1], item[0]))

    print("\nFinal rankings:")
    for rank, (team, points) in enumerate(rankings, 1):
        print(f"{rank}. {team}: {points} points")


if __name__ == "__main__":
    sports_scheduling_and_scoring()
