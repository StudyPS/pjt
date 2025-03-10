import sys

word_map = {}
N, M = map(int, sys.stdin.readline().split())
total_count = 0
for i in range(N):
    word = sys.stdin.readline().strip()
    word_map[word] = 1
for i in range(M):
    word = sys.stdin.readline().strip()
    
    if word_map.get(word) is not None:
        total_count += 1

print(total_count)
