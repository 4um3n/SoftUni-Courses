max_bad_appraisals = int(input())
problem_name = input()
last_problem = ""
appraisals_sum = 0
total_problems = 0
bad_appraisal_count = 0
is_enough = False

while problem_name != "Enough":
    current_appraisal = int(input())
    total_problems += 1
    appraisals_sum += current_appraisal
    last_problem = problem_name

    if current_appraisal <= 4:
        bad_appraisal_count += 1

    if bad_appraisal_count >= max_bad_appraisals:
        is_enough = True
        break

    problem_name = input()

if is_enough:
    print(f"You need a break, {max_bad_appraisals} poor grades.")
else:
    print(f"Average score: {appraisals_sum / total_problems:.2f}\n"
          f"Number of problems: {total_problems}\n"
          f"Last problem: {last_problem}")
