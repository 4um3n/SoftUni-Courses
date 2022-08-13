def resolve_expression(expression, start, end, last):
    if expression[start] == 'f':
        if expression[end - 4] in ['t', 'f']:
            if last == end - 4:
                return expression[end]

            last = end - 4
            return resolve_expression(expression, end - 4, end, last)

        return expression[end]

    if expression[start] == 't':
        start += 2
        end -= 2
        return resolve_expression(expression, start, end, last)

    return expression[start]


def main():
    expression = input().split()
    start = 0
    end = len(expression) - 1
    result = resolve_expression(expression, start, end, end)
    return result


if __name__ == '__main__':
    print(main())


# t ? t ? t ? 4 : 1 : 2 : 3
# t ? f ? t ? 4 : 3 : t ? f ? 100 : f ? 500 : 600 : f ? 300 : 400 : 1
