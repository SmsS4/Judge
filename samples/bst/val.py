n, q = map(int, input().split())
assert 1 <= n <= 1_000
assert 1 <= q <= 1_000
a = list(map(int, input().split()))
for x in a:
    assert 1 <= x <= 1_000_000_000
for i in range(q):
    x = int(input())
    assert 1 <= x <= 1_000_000_000
