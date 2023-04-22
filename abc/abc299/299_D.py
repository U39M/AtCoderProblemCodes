N = int(input())
lo, hi = 1, N
while lo + 1 < hi:
    mi = (lo + hi) // 2
    print('?', mi)
    S = int(input())
    if S == 0:
        lo = mi
    else:
        hi = mi
print('!', lo)
