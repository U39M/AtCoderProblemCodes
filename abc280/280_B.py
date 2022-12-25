n = int(input())
S = list(map(int, input().split()))
A = []

acc = 0

for i in range(n):
    A.append(S[i] - acc)
    acc += A[-1]

print(*A)
