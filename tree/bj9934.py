"""
9934 완전 이진트리
https://www.acmicpc.net/problem/9934
"""

import sys


N = int(sys.stdin.readline())
iplist = list(map(int, sys.stdin.readline().split()))
result_list = [[] for i in range(N)]


def sol(dept, iplist):

    midindex = len(iplist) // 2

    mid = iplist[midindex]
    result_list[dept].append(mid)
    if len(iplist) == 1:
        return

    sol(dept + 1, iplist[:midindex])
    sol(dept + 1, iplist[midindex + 1 :])


sol(0, iplist)
for t in result_list:
    for tt in t:
        print(tt, end=" ")
    print()
