import sys

DISTANCE = 20


def main():
    n = int(input())

    metros = [tuple()] * n
    for i in range(n):
        metros[i] = tuple(map(int, sys.stdin.readline().split()))

    m = int(input())
    stations = {}
    for i in range(m):
        station = tuple(map(int, sys.stdin.readline().split()))
        station_hash = area_hash(station)
        if stations.get(station_hash) is None:
            stations[station_hash] = [station]
        else:
            stations[station_hash].append(station)

    top = 0
    top_index = 0
    cached = {}

    # 14 * 2 + 15 * 2 - minimum modules sum for distance > 20 (any cases)
    minimum = 29

    for i, metro in enumerate(metros):
        local_top = 0
        near_stations = get_stations(stations, metro)
        if len(near_stations) < top:
            continue

        for station in near_stations:
            mx = metro[0] - station[0]
            my = metro[1] - station[1]
            if not -20 <= mx <= 20 or not -20 <= my <= 20 or mx + my >= minimum:
                continue

            distance = cached.get((mx, my))
            if distance is None:
                distance = mx ** 2 + my ** 2
                cached[(mx, my)] = distance

            if distance <= 400:
                local_top += 1

        if local_top > top:
            top = local_top
            top_index = i + 1

    print(top_index)


def area_hash(point):
    return point[0] - point[0] % DISTANCE, point[1] - point[1] % DISTANCE


def get_stations(stations, metro):
    point_hash = area_hash(metro)
    neighbours = [
        (point_hash[0] - DISTANCE, point_hash[1] + DISTANCE),  # top left
        (point_hash[0], point_hash[1] + DISTANCE),  # top center
        (point_hash[0] + DISTANCE, point_hash[1] + DISTANCE),  # top right
        (point_hash[0] - DISTANCE, point_hash[1]),  # center left
        point_hash,  # center center
        (point_hash[0] + DISTANCE, point_hash[1]),  # center right
        (point_hash[0] - DISTANCE, point_hash[1] - DISTANCE),  # bottom left
        (point_hash[0], point_hash[1] - DISTANCE),  # bottom center
        (point_hash[0] + DISTANCE, point_hash[1] - DISTANCE),  # bottom right
    ]

    near_stations = []
    for neighbour in neighbours:
        if stations.get(neighbour) is not None:
            near_stations += stations.get(neighbour)

    return near_stations


if __name__ == '__main__':
    main()
