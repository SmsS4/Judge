import sys

input = sys.stdin.readline
from collections import defaultdict


class Node:
    def __init__(self):
        self.cnt = 0
        self.next = [None] * 2


root = Node()


def add(x):
    root.cnt += 1
    cur = root
    for k in range(32, -1, -1):
        bit = (x >> k) & 1
        if not cur.next[bit]:
            cur.next[bit] = Node()
        cur = cur.next[bit]
        cur.cnt += 1


def remove(x):
    root.cnt -= 1
    cur = root
    for k in range(32, -1, -1):
        bit = (x >> k) & 1
        cur = cur.next[bit]
        cur.cnt -= 1


def query(x):
    cur = root
    ret = 0
    for k in range(32, -1, -1):
        bit = (x >> k) & 1
        if cur.next[bit ^ 1] and cur.next[bit ^ 1].cnt > 0:
            ret += (1 << k)
            cur = cur.next[bit ^ 1]
        else:
            cur = cur.next[bit]
    return ret


add(0)
q = int(input())
for _ in range(q):
    comm, x = input().split()
    x = int(x)
    if comm == '+':
        add(x)
    elif comm == '-':
        remove(x)
    else:
        print(query(x))
