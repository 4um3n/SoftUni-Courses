command, companies = input(), {}
while command != "End":
    company, employee_id = command.split(" -> ")
    if company not in companies:
        companies[company] = []
    
    if employee_id not in companies[company]:
        companies[company].append(employee_id)

    command = input()

for c, employees in sorted(companies.items()):
    print(f"{c}")
    for e in employees:
        print(f"-- {e}")