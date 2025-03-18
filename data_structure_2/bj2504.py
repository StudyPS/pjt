"""
백준 2504 괄호의 값
"""

import sys


def solution(full_string_split: list):
    stack = list()
    total = 0
    tmp = 1
    for i, t in enumerate(full_string_split):
        if t == "(":
            tmp *= 2
            stack.append(t)
        elif t == ")":
            if len(stack) == 0 or stack[-1] == "[":
                return 0
            if full_string_split[i - 1] == "(":
                total += tmp
            stack.pop()
            tmp //= 2
        elif t == "[":
            tmp *= 3
            stack.append(t)
        elif t == "]":
            if len(stack) == 0 or stack[-1] == "(":
                return 0
            if full_string_split[i - 1] == "[":
                total += tmp
            stack.pop()
            tmp //= 3
    if stack:
        return 0

    return total


full_string_split = list(sys.stdin.readline().strip())
print(solution(full_string_split))
