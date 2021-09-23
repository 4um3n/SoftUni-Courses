def expressions_maker(data: list, result=0, expression=""):
    if not data:
        return expression, result

    plus = expressions_maker(data[1:], result + data[0], expression + f"+{data[0]}")
    minus = expressions_maker(data[1:], result - data[0], expression + f"-{data[0]}")
    return plus + minus


numbers_data = list(map(int, input().split(", ")))
made_expressions = expressions_maker(numbers_data)
[print(f"{made_expressions[i]}={made_expressions[i+1]}") for i in range(0, len(made_expressions), 2)]
