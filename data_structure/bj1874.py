import sys
from collections import deque

N = int(sys.stdin.readline())

deq = deque([0])

last = 1
result_list = []
def loop(input_num, deq: deque):
    global last
    global result_list
    while deq:
        last_num = deq[-1]
        
        if input_num > last_num:
            deq.append(last)
            last += 1
            result_list.append("+")
        elif input_num == last_num:
            deq.pop()
            result_list.append("-")
            return 
        else:
            return "fuck"




for i in range(N):
    input_num = int(sys.stdin.readline())
    if loop(input_num, deq) == "fuck":
        print("NO")
        exit(0)

print(*result_list, sep='\n')