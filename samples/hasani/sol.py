import sys
sys.setrecursionlimit(300_000)

n, m = map(int, input().split())

if m == 0:
    print(3, n * (n - 1) * (n - 2) // 6)
    exit(0)

adj = [[] for _ in range(n)]
h = [-1] * n

for i in range(m):
    x, y = map(int, input().split())
    adj[x - 1].append(y - 1)
    adj[y - 1].append(x - 1)


def dfs(root):
    res = [1, 0]
    for x in adj[root]:
        if h[x] == -1:
            h[x] = h[root] + 1
            child = dfs(x)
            res[0] += child[1]
            res[1] += child[0]
        elif h[x] % 2 == h[root]%2 and x != root:
            # odd cycle
            print(0, 1)
            exit(0)
    return res


def cal_ans_cnt(x, y):
    if not x or not y:
        return 100, 100
    return x * y


cnt = 0
for i in range(n):
    if h[i] == -1:
        h[i] = 0
        dfs_res = dfs(i)
        if dfs_res[0] == 0 or dfs_res[1] == 0:
            continue
        cnt += dfs_res[0] * (dfs_res[0] - 1) // 2
        cnt += dfs_res[1] * (dfs_res[1] - 1) // 2
if cnt == 0:
    print(2, m * (n - 2))
else:
    print(1, cnt)
