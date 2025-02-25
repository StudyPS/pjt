"""
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

"""

from collections import deque
import sys

deq = deque()

loop_count = int(input())

for i in range(loop_count):
    req = sys.stdin.readline().split()
    key = req[0]
    if key == "push":
        deq.append(req[1])
    elif key == "pop":
        print(-1 if len(deq) == 0 else deq.popleft())
    elif key == "size":
        print(len(deq))
    elif key == "empty":
        print(1) if len(deq) == 0 else print(0)
    elif key == "front":
        print(-1 if len(deq) == 0 else deq[0])
    elif key == "back":
        print(-1 if len(deq) == 0 else deq[len(deq)-1])

