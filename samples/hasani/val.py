n, m = map(int, input().split())
assert 1 <= n <= 100_000
assert 0 <= m <= 100_000

edges = set()
for i in range(m):
    x, y = map(int, input().split())
    edges.add((min(x, y), max(x, y)))
    assert x != y
    assert 1 <= x <= n
    assert 1 <= y <= n

assert len(edges) == m