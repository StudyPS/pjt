import sys


class Node:
    def __init__(self, value):
        self.value = value  # 노드가 저장하는 데이터
        self.next = None    # 다음 노드를 가리키는 포인터
        self.prev = None    # 이전 노드를 가리키는 포인터


class Deque:
    def __init__(self):
        self.head = None  # 앞쪽 포인터
        self.tail = None  # 뒤쪽 포인터
        self.size = 0

    def append(self, value):
        """오른쪽 끝에 추가"""
        new_node = Node(value)
        if self.tail is None:  # 첫 요소 추가
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def appendleft(self, value):
        """왼쪽 끝에 추가"""
        new_node = Node(value)
        if self.head is None:  # 첫 요소 추가
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def pop(self):
        """오른쪽 끝에서 제거"""
        if self.tail is None:
            return -1
        value = self.tail.value
        self.tail = self.tail.prev
        if self.tail is None:  # 리스트가 비었을 경우
            self.head = None
        else:
            self.tail.next = None
        self.size -= 1
        return value

    def popleft(self):
        """왼쪽 끝에서 제거"""
        if self.head is None:
            return -1
        value = self.head.value
        self.head = self.head.next
        if self.head is None:  # 리스트가 비었을 경우
            self.tail = None
        else:
            self.head.prev = None
        self.size -= 1
        return value

    def __len__(self):
        return self.size
    
    def empty(self):
        """비어 있으면 1 아니면 0"""
        return 1 if self.size == 0 else 0
    
    def front(self):
        return str(self.head.value) if self.head is not None else -1
    
    def back(self):
        return str(self.tail.value) if self.tail is not None else -1

    def __repr__(self):
        values = []
        curr = self.head
        while curr:
            values.append(str(curr.value))
            curr = curr.next
        return "Deque([" + ", ".join(values) + "])"


deq = Deque()

loop_count = int(input())

for i in range(loop_count):
    req = sys.stdin.readline().split()
    key = req[0]
    if key == "push_front":
        deq.appendleft(req[1])
    elif key == "push_back":
        deq.append(req[1])
    elif key == "pop_front":
        print(-1 if len(deq) == 0 else deq.popleft())
    elif key == "pop_back":
        print(-1 if len(deq) == 0 else deq.pop())
    elif key == "size":
        print(len(deq))
    elif key == "empty":
        print(1) if len(deq) == 0 else print(0)
    elif key == "front":
        print(deq.front())
    elif key == "back":
        print(deq.back())

