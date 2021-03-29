import collections
n = int(input())
cnt = collections.defaultdict(int)
for i in range(n):
    type, x = input().split()
    x = int(x)
    assert 1 <= x <= 1_000_000_000
    if type == '+':
        cnt[x] += 1
    elif type == '-':
        cnt[x] -= 1
        assert cnt[x] >= 0
