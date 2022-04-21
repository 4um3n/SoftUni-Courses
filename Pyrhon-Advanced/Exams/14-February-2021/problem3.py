def stock_availability(flavours: list, command: str, *args):
    if command == "delivery":
        flavours.extend(args)

    elif command == "sell":
        if not args:
            flavours.pop(0)

        elif len(args) == 1 and isinstance(args[0], int):
            flavours = flavours[int(args[0]):]

        else:
            for order in args:
                while order in flavours:
                    flavours.remove(order)

    return flavours
