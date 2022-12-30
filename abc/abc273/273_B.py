x, k = map(int, input().split())
for i in range(k):
    if x % 10 >= 5:
        x = x // 10 + 1
    else:
        x = x // 10
print(x * 10 ** k)
