from typing import Optional


class QS:
    def __init__(self, tm:int, stack=True):
        self.tm = tm
        self.mem = []
        if stack:
            self.pop_ind = -1
        else:
            self.pop_ind = 0
        self.rem = 0
        self.current = None

    def do(self) -> Optional[int]:
        result = None
        if self.rem:
            self.rem -= 1
        if self.rem == 0:
            result = self.current
            if len(self.mem):
                self.current = self.pop()
                self.rem = self.tm
            else:
                self.current = None
        return result

    def push(self, x):
        self.mem.append(x)

    def pop(self) -> int:
        return self.mem.pop(self.pop_ind)


n, m = map(int, input().split())
t = list(map(int, input().split()))
types = list(map(int, input().split()))
qs = [QS(t[i], types[i] == 1) for i in range(n)]
for i in range(m):
    qs[0].push(i)
ans = [0] * m
tm = -1
done = 0
while done < m:
    tm += 1
    for i in range(n):
        nxt = qs[i].do()
        if nxt is not None:
            if i == n-1:
                ans[nxt] = tm
                done += 1
            else:
                qs[i+1].push(nxt)


print(*ans)


