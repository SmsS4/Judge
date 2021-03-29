import sys
from typing import Optional, List
sys.setrecursionlimit(10000)


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def go_to(self, value: int) -> Optional[int]:
        if value < self.value:
            return self.left
        if value > self.value:
            return self.right
        if value == self.value:
            return None

    def add_child(self, node: 'Node'):
        if node.value < self.value:
            if self.left:
                raise Exception('oh to')
            self.left = node
        if node.value > self.value:
            if self.right:
                raise Exception('baba')
            self.right = node
        if node.value == self.value:
            pass


class BST:
    def __init__(self):
        self.root = None

        self.__cal_h = -1

    def insert(self, value: int):
        node = Node(value)
        if not self.root:
            self.root = node
        cur = self.root
        while cur.go_to(value):
            cur = cur.go_to(value)
        cur.add_child(node)

    def get_left_most(self):
        self.__cal_h = -1
        return self.__get_left_most(self.root, 0)

    def __get_left_most(self, cur: Node, h: int):
        if cur is None:
            return 0
        ans = 0
        if h == self.__cal_h + 1:
            self.__cal_h += 1
            ans += cur.value
        return ans + self.__get_left_most(cur.left, h + 1) + self.__get_left_most(cur.right, h + 1)


n, q = map(int, input().split())
a = list(map(int, input().split()))
bst = BST()
for x in a:
    bst.insert(x)
print(bst.get_left_most())
for i in range(q):
    x = int(input())
    bst.insert(x)
    print(bst.get_left_most())
