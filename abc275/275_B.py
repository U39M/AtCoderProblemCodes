# coding: utf-8
# Your code here!

a, b, c, d, e, f = map(int, input().split())

ABC = a*b*c
DEF = d*e*f

if ABC >= DEF:
    ans = (ABC - DEF) % 998244353


print(ans)
