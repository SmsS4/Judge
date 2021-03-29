heap = [None]
n = int(input())
a = list(map(int, input().split()))
for x in a:
    heap.append(x)
    cur = len(heap) - 1
    while cur != 1 and heap[cur // 2] > heap[cur]:
        print(min(heap[cur // 2], heap[cur]), max(heap[cur // 2], heap[cur]))
        heap[cur // 2], heap[cur] = heap[cur], heap[cur // 2]
        cur //= 2
