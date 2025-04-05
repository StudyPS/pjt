import sys
from itertools import chain
from collections import defaultdict


def parse_input():
    cases = []
    current_tree = defaultdict(list)

    while True:
        line = sys.stdin.readline().strip()
        if not line:  # 공백이면 넘어가버림
            continue
        if line == "-1 -1":  # 실행 끝.
            break
        pairs = line.split("  ")
        for pair in pairs:
            if not pair.strip():
                continue
            u, v = pair.strip().split()
            if u == "0" and v == "0":
                cases.append(current_tree)
                current_tree = defaultdict(list)  # 입력받은 블록의 tree 초기화
                break
            current_tree[u].append(v)
    return cases


def is_tree(tree, index):
    keys = set(tree.keys())
    values = list(chain.from_iterable(tree.values()))
    value_set = set(values)
    all_nodes = keys | value_set

    if not all_nodes:  # 이딴게 트리?
        print(f"Case {index} is a tree.")
        return

    # Root 노드는 들어오는 간선이 없는 노드
    roots = [node for node in keys if node not in value_set]

    # 자식 노드가 둘 이상 부모를 가졌는지 검사
    if len(roots) != 1 or len(values) != len(value_set):
        print(f"Case {index} is not a tree.")
    else:
        print(f"Case {index} is a tree.")


cases = parse_input()
for idx, tree in enumerate(cases, 1):
    is_tree(tree, idx)
