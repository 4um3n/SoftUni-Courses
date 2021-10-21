steps_goal = 10000
steps_counter = 0

while steps_counter < steps_goal:
    current_steps = input()
    if current_steps == "Going home":
        current_steps = int(input())
        steps_counter += current_steps
        break

    current_steps = int(current_steps)
    steps_counter += current_steps

steps_diff = abs(steps_goal - steps_counter)

if steps_counter >= steps_goal:
    print(f"Goal reached! Good job!\n"
          f"{steps_diff} steps over the goal!")
else:
    print(f"{steps_diff} more steps to reach goal.")
