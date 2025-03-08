
import operator
import sys
from collections import deque

# 오퍼레이터 선언
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


N = int(sys.stdin.readline())
input_num = []
renum = deque()

foo = list(sys.stdin.readline().strip())

for i in range(N):
    input_num.append(int(sys.stdin.readline()))

for i in foo:
    if i.isalpha():
        renum.append(input_num[ord(i)-65])
    else:
        Y = renum.pop()
        X = renum.pop()
        res = ops[i](X, Y)
        renum.append(res)

print(f"{renum.pop():.2f}")
