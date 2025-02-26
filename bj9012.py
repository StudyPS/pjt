
import sys

def solution(line: str):

    stack = list()
    arry = list(line.strip('\n'))
    for x in arry:
        if x == "(":
            stack.append(x)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                return "NO"
    return "YES" if len(stack) == 0 else "NO"


loop_count = int(input())

for i in range(loop_count):
    str = sys.stdin.readline()
    print(solution(str))



