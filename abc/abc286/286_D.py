N, X = map(int, input().split())
dp = [[-1] * (X+1) for i in range(N+1)]
dp[0][0] = 0
for i in range(1, N+1):
    A, B = map(int, input().split())
    for b in range(X+1):
        for j in range(B+1):
            if b+(A*j) <= X and dp[i-1][b] >= 0:
                dp[i][b + (A*j)] = 1
if dp[-1][-1] == 1:
    print("Yes")
else:
    print("No")
