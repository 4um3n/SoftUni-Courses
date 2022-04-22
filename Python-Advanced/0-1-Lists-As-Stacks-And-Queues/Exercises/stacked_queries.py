from collections import deque

stack = deque()
for _ in range(int(input())):
    command = input().split()
    if "1" in command:
        n = int(command[1])
        stack.append(n)
    
    elif "2" in command and len(stack) > 0:
        stack.pop()
    
    elif "3" in command and len(stack) > 0:
        print(max(stack))
    
    elif "4" in command and len(stack) > 0:
        print(min(stack))


print(', '.join(str(stack[i]) for i in range(len(stack) - 1, -1, -1)))
