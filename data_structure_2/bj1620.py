
import sys

N, M = map(int, sys.stdin.readline().split())

po_list = [0]
po_map = {}
for i in range(1, N+1):
    pokeymon = sys.stdin.readline().strip()
    po_list.append(pokeymon)
    po_map[pokeymon] = i

for i in range(M):
    input = sys.stdin.readline().strip()
    if input.isdigit():
        print(po_list[int(input)])
    else:
        print(po_map[input])
