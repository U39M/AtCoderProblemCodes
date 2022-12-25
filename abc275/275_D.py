# coding: utf-8
# Your code here!
from functools import lru_cache

N = int(input())

@lru_cache(maxsize=1000)
def func(k):
    if k < 1:
        return 1
    return func(k // 2) + func(k // 3)

print(func(N))
    