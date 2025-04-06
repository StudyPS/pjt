import sys


# 입력 받기 .
N = int(sys.stdin.readline())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    x, y = map(int, sys.stdin.readline().split())
    tree[y].append(x)
    tree[x].append(y)

# 질의 응답
N = int(sys.stdin.readline())
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    if x == 2:  # 단절선은 어딜 끊어도 두개의 트리로 나누어짐
        print("yes")
    elif x == 1:
        if len(tree[y]) >= 2:  # 연결된 간선이 2개 이상이면
            print("yes")
        else:
            print("no")
