def get_min_platforms_count_greedy(arrival_times, departure_times):
    platforms = 1
    current_platforms = 1
    trains_count = len(arrival_times)
    last = departure_times[0]

    arrival_times.sort()
    departure_times.sort()

    arr_idx = 1
    dep_idx = 0

    while arr_idx < trains_count and dep_idx < trains_count:
        if arrival_times[arr_idx] <= departure_times[dep_idx]:
            if arrival_times[arr_idx] == last:
                arr_idx += 1
                continue
            arr_idx += 1
            current_platforms += 1
        elif departure_times[dep_idx] < arrival_times[arr_idx]:
            dep_idx += 1
            current_platforms -= 1
            last = departure_times[dep_idx]

        platforms = max(current_platforms, platforms)

    return platforms


def main():
    arrival_times = [float(n) for n in input().split()]
    departure_times = [float(n) for n in input().split()]
    return get_min_platforms_count_greedy(arrival_times, departure_times)


if __name__ == '__main__':
    print(main())


# 2.00 2.10 3.00 3.20 3.50 5.00
# 2.30 3.40 3.20 4.30 4.00 5.20
