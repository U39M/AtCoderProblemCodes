# coding: utf-8
# Your code here!
h, w = map(int, input().split())

s = []
counter = 0

for i in range(h):
    s.append(input())
    counter += s[i].count('#')
print(counter)
