"""
push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""

import sys
from collections import deque

deq = deque()

loop_count = int(input())

for i in range(loop_count):
    req = sys.stdin.readline().split()
    key = req[0]
    if key == "push_front":
        deq.appendleft(req[1])
    elif key == "push_back":
        deq.append(req[1])
    elif key == "pop_front":
        print(-1 if len(deq) == 0 else deq.popleft())
    elif key == "pop_back":
        print(-1 if len(deq) == 0 else deq.pop())
    elif key == "size":
        print(len(deq))
    elif key == "empty":
        print(1) if len(deq) == 0 else print(0)
    elif key == "front":
        print(-1 if len(deq) == 0 else deq[0])
    elif key == "back":
        print(-1 if len(deq) == 0 else deq[len(deq)-1])

