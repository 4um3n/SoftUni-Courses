def stock_availability(flavours: list, order_type: str, *args):
    if order_type == "delivery":
        if not args:
            return flavours

        flavours.append(args[0])
        return stock_availability(flavours, order_type, *args[1:])

    elif order_type == "sell":
        if not args:
            return flavours[1:]

        elif isinstance(args[0], int):
            return flavours[args[0]:]

        for order in args:
            while order in flavours:
                flavours.remove(order)

        return flavours
