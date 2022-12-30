# coding: utf-8
# Your code here!

h, w = map(int, input().split())
ans = [0] * w

for i in range(h):
    c = list(input())
    for j in range(w):
        if c[j] == '#':
            ans[j] += 1
print(*ans)
