N, X = map(int, input().split())
A = list(map(int, input().split()))
S = set(A)
ans = "No"
for i in S:
	if i - X in S:
		ans = "Yes"
print(ans)
