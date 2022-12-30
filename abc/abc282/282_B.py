# coding: utf-8
# Your code here!

n, m = map(int, input().split())
s = []

for i in range(n):
    s.append(input())

ans = 0

for i in range(n):
    for j in range(i+1,n):
        cnt = 0
        for k in range(m):
            cnt += (s[i][k] == 'o' or s[j][k] == 'o')
        if cnt == m:
            ans += 1
print(ans)
        