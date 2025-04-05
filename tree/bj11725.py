"""
트리의 부모 찾기.
https://www.acmicpc.net/problem/11725
"""

from collections import deque
import sys

sys.setrecursionlimit(10**6)


def input_text(N):
    input_list = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)
    for _ in range(1, N):
        x, y = map(int, sys.stdin.readline().split())
        input_list[x].append(y)
        input_list[y].append(x)
    return input_list, visited


def dfs(index, graph, visited):
    for i in graph[index]:
        if visited[i] == 0:
            visited[i] = index
            dfs(i, graph, visited)
    return visited


def bfs(start, graph, visited):
    deq = deque([start])
    while deq:
        node = deq.popleft()
        for value in graph[node]:
            if visited[value] == 0:
                visited[value] = node
                deq.append(value)
    return visited


N = int(sys.stdin.readline())
input_list, visited = input_text(N)

# result = dfs(1, input_list, visited) dfs보다 bfs가 더 성능이 좋음
# dfs : 308ms
# bfs : 268ms
result = bfs(1, input_list, visited)
for x in range(2, N + 1):
    print(result[x])
