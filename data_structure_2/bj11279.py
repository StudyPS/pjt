import heapq
import sys

N = int(sys.stdin.readline())

hq = []
for i in range(N):
    nu = int(sys.stdin.readline())
    if nu == 0:
        print(-1 * int(heapq.heappop(hq)) if len(hq) != 0 else 0)
    else:
        value = nu * -1
        heapq.heappush(hq, value)
