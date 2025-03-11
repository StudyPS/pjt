"""
5
12 7 9 15 5
13 8 11 19 6
21 10 26 31 16
48 14 28 35 25
52 20 32 41 49

최소힙 사용 이진트리
"""

import heapq
import sys

N = int(sys.stdin.readline())

hq = []

for i in range(N):
    i_list = list(map(int, sys.stdin.readline().strip().split()))

    for j in i_list:
        if len(hq) < N:  # N번째로 큰값을 구해야하기 때문에 N개만 저장.
            heapq.heappush(hq, j)
        else:
            if (
                hq[0] < j
            ):  # [0]의 수는 가장 작은 수이지만 크기를 N개로 제한하여 [0]은 N번째 큰 값이 됨.
                heapq.heappop(hq)
                heapq.heappush(hq, j)

print(hq[0])
