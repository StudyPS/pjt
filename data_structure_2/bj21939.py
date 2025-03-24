"""
문제 추천 시스템 Version 1
https://www.acmicpc.net/problem/21939

"""

import heapq
import sys
from collections import defaultdict

max_hq, min_hq = [], []
solved = defaultdict(int)


def solution(loop_count):
    for _ in range(loop_count):
        command = sys.stdin.readline().strip().split()
        option = command[0]
        if option == "recommend":
            value = int(command[1])
            if value == -1:
                while solved[min_hq[0][1]] != 0:
                    solved[min_hq[0][1]] -= 1
                    heapq.heappop(min_hq)
                print(min_hq[0][1])

            elif value == 1:
                while solved[abs(max_hq[0][1])] != 0:
                    solved[abs(max_hq[0][1])] -= 1
                    heapq.heappop(max_hq)
                print(abs(max_hq[0][1]))
        elif option == "add":
            value = int(command[1])
            value2 = int(command[2])
            heapq.heappush(
                max_hq,
                (
                    -value2,
                    -value,
                ),
            )
            heapq.heappush(min_hq, (value2, value))
        elif option == "solved":
            value = int(command[1])
            solved[value] += 1


N = int(sys.stdin.readline())

for i in range(N):
    lv, rv = map(int, sys.stdin.readline().split())
    heapq.heappush(
        max_hq,
        (
            -rv,
            -lv,
        ),
    )
    heapq.heappush(min_hq, (rv, lv))


loop_count = int(sys.stdin.readline())
solution(loop_count)
