employee_happiness = [int(n) for n in input().split()]
factor = int(input()) 
employee_happiness = [n * factor for n in employee_happiness]
average_happiness = sum(employee_happiness) / len(employee_happiness)
happy_employees = [n for n in employee_happiness if n >= average_happiness]
if len(happy_employees) >= len(employee_happiness) // 2:
    print(f"Score: {len(happy_employees)}/{len(employee_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(employee_happiness)}. Employees are not happy!")
