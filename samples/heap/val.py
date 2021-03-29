n = int(input())
a = list(map(int, input().split()))
assert len(a) == n
a = list(sorted(a))
for i in range(len(a)):
    assert a[i] == i+1