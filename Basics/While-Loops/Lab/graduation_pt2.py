student_name = input()
bad_appraisals = 0
appraisals_sum = 0
current_class_year = 1

while bad_appraisals < 2 and current_class_year <= 12:
    year_appraisal = float(input())

    if year_appraisal < 4:
        bad_appraisals += 1
        continue

    appraisals_sum += year_appraisal
    current_class_year += 1

if current_class_year <= 12:
    print(f"{student_name} has been excluded at {current_class_year} grade")
else:
    print(f"{student_name} graduated. Average grade: {appraisals_sum / 12:.2f}")
