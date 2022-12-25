# coding: utf-8
# Your code here!

a, b = map(int, input().split())

if a < 11:
    s = b/a
    s = '{:.3f}'.format(s)

print(s)
