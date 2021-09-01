r_count = int(input())
free_chairs, is_no_more_chairs = 0, False
for r in range(1, r_count + 1):
    chairs, visitors = input().split()
    chairs, visitors = len(chairs), int(visitors)
    if chairs < visitors:
        print(f"{abs(chairs - visitors)} more chairs needed in room {r}")
        is_no_more_chairs = True
        continue

    free_chairs += chairs - visitors

if not is_no_more_chairs:
    print(f"Game On, {free_chairs} free chairs left")
