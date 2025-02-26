
import sys

stack = list()

loop_count = int(input())

for i in range(loop_count):
    req = sys.stdin.readline().split()
    key = req[0]
    if key == "push":
        stack.append(req[1])
    elif key == "pop":
        print(-1 if len(stack) == 0 else stack.pop())
    elif key == "size":
        print(len(stack))
    elif key == "empty":
        print(1) if len(stack) == 0 else print(0)
    elif key == "top":
        print(-1 if len(stack) == 0 else stack[-1])

