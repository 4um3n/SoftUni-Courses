def flights(*args, flights_data=dict()):
    if args[0] == "Finish" or not args:
        return flights_data

    if args[0] not in flights_data:
        flights_data[args[0]] = 0

    flights_data[args[0]] += int(args[1])
    return flights(*args[2:], flights_data=flights_data)
