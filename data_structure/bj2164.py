'''
카드 2

N 이 주어질 때

1번 카드가 제일 위에 N번 카드가 제일 아래인 상태로 놓여짐 

N=4 일 경우
0. 1,2,3,4
1. 2,3,4
2. 3,4,2
3. 4,2
4. 2,4
5. 4

'''

import sys
from collections import deque

N = int(sys.stdin.readline())

deq = deque(x for x in range(1,N+1))

while len(deq) > 1:
    deq.popleft()
    tmp = deq.popleft()
    deq.append(tmp)
    

print(deq[0])