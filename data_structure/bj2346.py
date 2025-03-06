import sys
from collections import deque

N = int(sys.stdin.readline())

p_list = tuple(map(int, (sys.stdin.readline().split()))) #종이 목록 
liste = deque(range(1, N+1)) # 1, 2, ... N

result = []

for i in range(N):
    a = liste.popleft() # 0번이 터뜨릴 풍선으로 오게끔.
    pick = p_list[int(a-1)] #터뜨린 풍선의 종이
    result.append(a) # 결과에 추가 
    rotate = int(pick-1 if pick > 0 else pick) * -1 # 음수일 경우 오른쪽으로 이동
    
    liste.rotate(rotate)

print(" ".join(map(str, result)))


