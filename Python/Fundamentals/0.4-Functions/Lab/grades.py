def print_grade(appraisal):
    if appraisal < 3:
        return "Fail"
    elif appraisal < 3.50:
        return "Poor"
    elif appraisal <  4.50:
        return "Good"
    elif appraisal < 5.50:
        return "Very Good"
    elif appraisal <= 6:
        return "Excellent"


print(print_grade(float(input())))