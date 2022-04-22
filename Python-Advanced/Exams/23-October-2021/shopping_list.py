def shopping_list(budget: int, **kwargs):
    if budget < 100:
        return f"You do not have enough budget."

    res = []
    for k, v in kwargs.items():
        p, q = [float(n) for n in v]
        price = p * q
        if price > budget:
            continue

        res.append(f"You bought {k} for {price:.2f} leva.")
        budget -= price

        if len(res) >= 5:
            break

    return '\n'.join(res)
