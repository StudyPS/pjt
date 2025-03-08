import sys
from collections import deque


def sol(array, target):
    que = deque((key, value) for key, value in enumerate(array))
    
    ord = sorted(array, reverse=True)
    count = 0

    while que:
        x, y = que.popleft()

        if(y == ord[count]):
            count += 1
            if(x == target):
                return count
        else:
            que.append((x,y))



N = int(sys.stdin.readline())
for i in range(N):
    x,y = map(int, sys.stdin.readline().split())
    arry = list(sys.stdin.readline().split())
    print(sol(arry, y))



# test = [1,1,9,1,1,1]
# print(sol(test, 0))