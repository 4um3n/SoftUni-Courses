jury_count = int(input())
presentation = input()
total_appraisals_container = 0
total_presentations_count = 0

while presentation != "Finish":
    total_presentations_count += 1
    current_average_appraisal = 0

    for i in range(jury_count):
        current_appraisal = float(input())
        current_average_appraisal += current_appraisal

    current_average_appraisal /= jury_count
    print(f"{presentation} - {current_average_appraisal:.2f}.")
    total_appraisals_container += current_average_appraisal
    presentation = input()

total_appraisals_container /= total_presentations_count
print(f"Student's final assessment is {total_appraisals_container:.2f}.")
