"""
https://www.acmicpc.net/problem/1991
트리 순회
"""

# 입력 받기


import sys

RESULT = ["", "", ""]


# 전위 순회
def preorder(node):
    if node != ".":
        RESULT[0] += node
        preorder(tree[node][0])
        preorder(tree[node][1])


# 중위 순회
def inorder(node):
    if node != ".":
        inorder(tree[node][0])
        RESULT[1] += node
        inorder(tree[node][1])


# 후위 순회
def postorder(node):
    if node != ".":
        postorder(tree[node][0])
        postorder(tree[node][1])
        RESULT[2] += node


N = int(sys.stdin.readline())

tree = {}

for _ in range(N):
    root, left, right = map(str, sys.stdin.readline().split())
    tree[root] = (left, right)
preorder("A")
inorder("A")
postorder("A")
print(RESULT[0])
print(RESULT[1])
print(RESULT[2])
