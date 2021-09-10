from typing import Optional, List


def main():
    n = int(input().strip())

    schedule = [None for _ in range(n)]  # type: List[Optional[tuple]]

    for i in range(n):
        begin, end = map(float, input().strip().split())
        schedule[i] = (begin, end)

    schedule = sorted(schedule, key=lambda e: (e[1], e[0]))

    max_events = 0
    events = []
    time = 0.0
    for event in schedule:
        if event[0] >= time:
            time = event[1]
            max_events += 1
            events.append(event)

    print(str(max_events))
    for event in events:
        print(f"{event[0]:g} {event[1]:g}")


if __name__ == '__main__':
    main()
