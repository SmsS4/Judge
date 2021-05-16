n, m = map(int, input().split())
assert 1 <= n <= 100_000
assert 0 <= m <= 100_000

edges = set()
for i in range(m):
    x, y, w = map(int, input().split())
    edges.add((min(x, y), max(x, y)))
    assert 1 <= w <= 1_000_000_000
    assert x != y
    assert 0 <= x <= n+1
    assert 0 <= y <= n+1

assert len(edges) == m