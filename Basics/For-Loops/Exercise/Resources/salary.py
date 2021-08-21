open_browser_tabs_count = int(input())
salary = int(input())
is_salary_lost = False

for i in range(open_browser_tabs_count):
    website = input()

    if website == "Facebook":
        salary -= 150
    elif website == "Instagram":
        salary -= 100
    elif website == "Reddit":
        salary -= 50

    if salary <= 0:
        is_salary_lost = True
        print(f"You have lost your salary.")
        break

if not is_salary_lost:
    print(f"{salary}")

