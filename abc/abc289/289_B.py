import sys
from collections import deque, Counter
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353

n, m = mi()

a = li()

p = list(range(1, n + 1))

s = []
ans = []
for v in p:
    s.append(v)
    if v not in a:
        while s:
            ans.append(s.pop())

print(*ans)