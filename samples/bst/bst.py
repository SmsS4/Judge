
import sys
from collections import deque
sys.setrecursionlimit(10000)

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key =key


def insertion(root , key):
    if root is None:
        return Node(key)
    else:
        if root.key == key:
            return root
        elif root.key < key:
            root.right = insertion(root.right, key)
        else:
            root.left = insertion(root.left, key)
    return root

def leftmost(root):
    if root is None:
        return

    q = deque()
    q.append(root)
    sum_leftmost_nodes = 0

    while q:
        for i in range(len(q)):
            temp = q[0]
            q.popleft()

            if i == 0:
                sum_leftmost_nodes += temp.key
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)

    return sum_leftmost_nodes


# ls = input().split(" ")
n = int(input())
tree = input().split(" ")
q = int(int(input()))

for i in range(len(tree)):
    tree[i] = int(tree[i])

root = Node(tree[0])
for i in range(len(tree) - 1):
    root = insertion(root, tree[i + 1])

print(leftmost(root))


while q != 0:
    c = int(input())
    insertion(root, c)
    print(leftmost(root))
    q -= 1






