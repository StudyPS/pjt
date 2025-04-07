"""
트리
https://www.acmicpc.net/problem/1068
"""

from collections import defaultdict


_ = int(input())
parents = list(map(int, input().split()))
remove_node = int(input())

tree = defaultdict(list)
parent_map = {}
root = None

for child, parent in enumerate(parents):
    if parent == -1:
        root = child
    else:
        tree[parent].append(child)
        parent_map[child] = parent

# 루트 노드를 지우면 전체 삭제
if remove_node == root:
    print(0)
    exit()

# 연결 끊기 (부모 노드에서 자식 삭제)
parent = parent_map.get(remove_node)
if parent is not None:
    tree[parent].remove(remove_node)


# 리프 노드 세기
def count_leaves(node):
    if not tree[node]:  # 자식이 없으면 리프노드
        return 1
    count = 0
    for child in tree[node]:
        count += count_leaves(child)
    return count


print(count_leaves(root))
