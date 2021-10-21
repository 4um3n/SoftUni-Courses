def add_submission(user: str, language: str, points: int, results: dict):
    if user not in results['users']:
        results['users'][user] = []

    if language not in results['submissions']:
        results['submissions'][l] = 0

    results['users'][user].append(points)
    results['submissions'][l] += 1
    return results



command, results_data = input(), {"users": {}, "submissions": {}}
while command != "exam finished":
    command = command.split("-")
    if "banned" in command:
        u = command[0]
        del results_data['users'][u]
    
    else:
        u, l, p = command
        results_data = add_submission(u, l, int(p), results_data)
    
    command = input()

print(f"Results:")
for u, p in sorted(results_data['users'].items(), key=lambda x: (-max(x[1]), x[0])):
    print(f"{u} | {max(p)}")

print(f"Submissions:")
for l, c in sorted(results_data['submissions'].items(), key=lambda x: (-x[1], x[0])):
    print(f"{l} - {c}")
