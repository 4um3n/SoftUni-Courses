contests_passwords, contests = {}, {}
command = input()
while command != "end of contests":
    contest, password = command.split(":")
    contests_passwords[contest] = password
    command = input()

command = input()
while command != "end of submissions":
    contest, password, username, points = command.split("=>")
    points = int(points)
    if contest not in contests_passwords or password != contests_passwords[contest]:
        command = input()
        continue

    if username not in contests:
        contests[username] = {}
    
    if contest not in contests[username] or contests[username][contest] < points:
        contests[username][contest] = points
    
    command = input()

candidates_total_points = {sum(i.values()): u for u, i in contests.items()}
best_candidate = candidates_total_points[max(candidates_total_points.keys())]
print(f"Best candidate is {best_candidate} with total {max(candidates_total_points.keys())} points.\nRanking:")
for u, contests_data in sorted(contests.items()):
    print(u)
    for l, p in sorted(contests_data.items(), key=lambda x: -x[1]):
        print(f"#  {l} -> {p}")
