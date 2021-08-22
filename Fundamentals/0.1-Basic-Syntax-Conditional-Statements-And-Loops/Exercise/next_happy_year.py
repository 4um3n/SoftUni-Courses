year = int(input())

for current_year in range(year + 1, 999999999):
    is_happy_year = True
    control_year = []

    for i in str(current_year):

        if i in control_year:
            is_happy_year = False
            break
        else:
            control_year.append(i)

    if is_happy_year:
        print(current_year)
        break
