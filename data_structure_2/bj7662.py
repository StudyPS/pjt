import heapq
import sys

N = int(sys.stdin.readline())


def sol1(loop_count):
    max_hq, min_hq = [], []
    visited = [False] * loop_count
    for i in range(loop_count):
        option, value = sys.stdin.readline().strip().split()
        value = int(value)
        if option == "I":
            heapq.heappush(max_hq, (-value, i))
            heapq.heappush(min_hq, (value, i))
            visited[i] = True
        elif option == "D":
            if value == -1:
                while min_hq and not visited[min_hq[0][1]]:
                    heapq.heappop(min_hq)
                if min_hq:
                    visited[min_hq[0][1]] = False
                    heapq.heappop(min_hq)
            elif value == 1:
                while max_hq and not visited[max_hq[0][1]]:
                    heapq.heappop(max_hq)
                if max_hq:
                    visited[max_hq[0][1]] = False
                    heapq.heappop(max_hq)
    while min_hq and not visited[min_hq[0][1]]:
        heapq.heappop(min_hq)
    while max_hq and not visited[max_hq[0][1]]:
        heapq.heappop(max_hq)
    if not min_hq or not max_hq:
        return "EMPTY"
    return f"{-max_hq[0][0]} {min_hq[0][0]}"


for i in range(N):
    loop_count = int(sys.stdin.readline())
    print(sol1(loop_count))
