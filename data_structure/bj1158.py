import sys

N, K = map(int, sys.stdin.readline().split())

c = [x for x in range(1,N+1)]

result_list = []
K-=1
last_index = 0
# for x in range(N):
while len(c) > 1:

    if len(result_list) == 0:
        last_index = K
    else:
        last_index += K 
        last_index = last_index % len(c)
    # print(last_index)
    # print(c)
    result_list.append(c.pop(last_index))

result_list.append(c.pop(0))
stl = ', '.join(map(str, result_list))

print(f'<{stl}>')
