import math

income_leva = float(input())
average_grade = float(input())
minimum_wage = float(input())

social_scholarship = 0.35 * minimum_wage
excellent_scholarship = average_grade * 25

if average_grade <= 4.50 or income_leva >= minimum_wage:
    print(f"You cannot get a scholarship!")
elif average_grade < 5.50 and income_leva < minimum_wage:
    print(f"You get a Social scholarship {math.floor(social_scholarship)} BGN")
elif average_grade >= 5.50:
    if income_leva >= minimum_wage:
        print(f"You get a scholarship for excellent results {math.floor(excellent_scholarship)} BGN")
    else:
        if social_scholarship > excellent_scholarship:
            print(f"You get a Social scholarship {math.floor(social_scholarship)} BGN")
        elif excellent_scholarship >= social_scholarship:
            print(f"You get a scholarship for excellent results {math.floor(excellent_scholarship)} BGN")
