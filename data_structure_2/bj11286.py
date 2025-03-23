import heapq
import sys

N = int(sys.stdin.readline())

main_hq = []
dic: dict[int, list[int]] = {}
for i in range(N):
    n = int(sys.stdin.readline())
    if n == 0:  # 입력이 0 일 경우 pop
        if len(main_hq) == 0:
            print(0)
        else:
            val = heapq.heappop(main_hq)
            # if p_hq[0] == val
    elif n != 0:
        heapq.heappush(main_hq, abs(n))
        if abs(n) in dic:
            dic[abs(n)].append(n)
        else:
            dic[abs(n)] = [n]
