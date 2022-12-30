# coding: utf-8
# Your code here!

s = input()

vCounter = s.count("v")
wCounter = s.count("w")

underV = vCounter
underW = wCounter * 2

print(underW + underV)
