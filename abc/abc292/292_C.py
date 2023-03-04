n = int(input())
pp = [0] * (n + 1)
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a * b > n:
            break
        pp[a * b] += 1
ans = sum(pp[i] * pp[n - i] for i in range(1, n + 1))
print(ans)
