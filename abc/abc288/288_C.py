import sys
sys.setrecursionlimit(10**6)


def dfs(v, last):
    global ans
    for i in G[v]:
        if i == last:
            continue
        if flag[i]:
            ans += 1
            continue
        flag[i] = True
        dfs(i, v)


N, M = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

flag = [False] * N
ans = 0

for i in range(N):
    if flag[i]:
        continue
    flag[i] = True
    dfs(i, -1)

print(ans//2)
