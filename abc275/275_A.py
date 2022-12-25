# coding: utf-8
# Your code here!

N = int(input())
H = list(map(int, input().split()))

tallest = 0
tallestNum = 0

for i in range(N):
    if H[i] > tallest:
        tallest = H[i]
        tallestNum = i + 1

print(tallestNum)
