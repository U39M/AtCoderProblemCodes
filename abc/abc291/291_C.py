#import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

if __name__ == "__main__":

    n = I()
    s = S()

    x = y = 0
    log = {(x,y)}

    for i in s:
        if i == "R":
            x += 1
        elif i == "L":
            x -= 1
        elif i == "U":
            y += 1
        elif i == "D":
            y -= 1
        
        if (x,y) in log:
            print("Yes")
            exit()
        log.add((x,y))
    print("No")


