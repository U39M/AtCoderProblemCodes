```
import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
N = I()
A = [LI() for _ in range(N)]import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
N = I()
A = [LI() for _ in range(N)]
```

input()より、sys.stdin.readline().rstrip()のほうが速度が良い
Iはintの標準入力
LIはlistの標準入力(1行n列)
Sは標準入力(文字型とか)
LSはlistの標準入力