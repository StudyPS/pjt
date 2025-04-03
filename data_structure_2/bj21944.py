import heapq
import sys

input = sys.stdin.readline

# 각 난이도, 알고리즘 유형별로 최소/최대 힙 관리
max_g_heap = [[] for _ in range(101)]  # 알고리즘 유형별 최대 힙
min_g_heap = [[] for _ in range(101)]  # 알고리즘 유형별 최소 힙
max_l_heap = [[] for _ in range(101)]  # 난이도별 최대 힙
min_l_heap = [[] for _ in range(101)]  # 난이도별 최소 힙

# 문제번호별 난이도 및 알고리즘 유형
l_lookup = [0] * 100001
g_lookup = [0] * 100001

# 삭제된 문제를 추적하는 집합
removed = set()


def add(p, l, g):
    """
    문제를 추가하고, 해당 문제에 대한 우선순위 힙에 삽입
    """
    lpg = l << 24 | p << 7 | g  # l, p, g를 합쳐 하나의 고유한 값 생성

    # 삭제된 문제라면 해당 삭제 기록 제거
    if is_removed(lpg):
        removed.remove(lpg)

    # 각 힙에 문제를 삽입 (최소, 최대 힙에 문제를 추가)
    heapq.heappush(max_g_heap[g], -lpg)
    heapq.heappush(min_g_heap[g], lpg)
    heapq.heappush(max_l_heap[l], -lpg)
    heapq.heappush(min_l_heap[l], lpg)

    # 문제번호-난이도, 문제번호-알고리즘 유형 매핑
    l_lookup[p] = l
    g_lookup[p] = g


def remove(p, l, g):
    """
    문제를 삭제되었음으로 표시
    실제 힙에서 삭제하는 대신, 삭제된 문제를 추적
    """
    removed.add(l << 24 | p << 7 | g)


def is_removed(lpg):
    """
    문제가 삭제되었는지 확인
    """
    return abs(lpg) in removed


def efficient_top(target_heap):
    """
    힙에서 유효한 최상위 문제를 반환 (삭제된 문제는 제외)
    """
    while target_heap and is_removed(target_heap[0]):
        heapq.heappop(target_heap)

    if target_heap:
        return (abs(target_heap[0]) >> 7) & (
            (1 << 17) - 1
        )  # p가 위치하는 가운데 17비트만 구함.
    return None


n = int(input())
for _ in range(n):
    p, l, g = map(int, input().split())
    add(p, l, g)

q = int(input())
for _ in range(q):
    cmd = input().split()

    if cmd[0] == "recommend":
        # recommend G x
        G, x = int(cmd[1]), int(cmd[2])
        if x == 1:
            print(efficient_top(max_g_heap[G]))  # 가장 어려운 문제
        else:
            print(efficient_top(min_g_heap[G]))  # 가장 쉬운 문제

    elif cmd[0] == "recommend2":
        # recommend2 x
        x = int(cmd[1])
        if x == 1:
            # 가장 어려운 문제 (난이도 기준)
            for i in range(100, 0, -1):
                if (a := efficient_top(max_l_heap[i])) is not None:
                    print(a)
                    break
        else:
            # 가장 쉬운 문제 (난이도 기준)
            for i in range(1, 101):
                if (a := efficient_top(min_l_heap[i])) is not None:
                    print(a)
                    break

    elif cmd[0] == "recommend3":
        # recommend3 x L
        x, L = int(cmd[1]), int(cmd[2])
        if x == 1:
            # 난이도가 L 이상인 문제 중 가장 쉬운 문제
            for i in range(L, 101):
                if (a := efficient_top(min_l_heap[i])) is not None:
                    print(a)
                    break
            else:
                print(-1)
        else:
            # 난이도가 L 미만인 문제 중 가장 어려운 문제
            for i in range(L - 1, 0, -1):
                if (a := efficient_top(max_l_heap[i])) is not None:
                    print(a)
                    break
            else:
                print(-1)

    elif cmd[0] == "add":
        # 문제 추가
        p, l, g = int(cmd[1]), int(cmd[2]), int(cmd[3])
        add(p, l, g)

    else:  # "solved"
        # 문제 해결 (삭제)
        p = int(cmd[1])
        remove(p, l_lookup[p], g_lookup[p])
