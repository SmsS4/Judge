n = int(input())
a = list(map(int, input().split()))


def count_inv(l, r) -> int:
    res = 0
    cnt = [0] * 102
    for i in range(n):
        cnt[a[i]] += 1
        L = min(101, a[i]*2)
        for j in range(L, 101):
            if j >= 2*a[i]:
                res += cnt[j]
    return res
    if l == r - 1:
        return 0
    mid = (l + r) // 2
    res = count_inv(l, mid) + count_inv(mid, r)
    L = l
    R = mid
    while L < mid and R < r:
        if a[L] >= 2 * a[R]:
            R += 1
        else:
            res += R - mid
            L += 1
    while L < mid:
        res += R - mid
        L += 1

    L = l
    R = mid
    b = []
    while L < mid and R < r:
        if a[L] > a[R]:
            b.append(a[R])
            R += 1
        else:
            b.append(a[L])
            L += 1
    while L < mid:
        b.append(a[L])
        L += 1
    while R < r:
        b.append(a[R])
        R += 1
    for i in range(len(b)):
        a[l + i] = b[i]
    return res


print(count_inv(0, n))
