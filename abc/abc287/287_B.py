if __name__ == "__main__" :
    n, m = map(int, input().split())
    s = [input()[3:] for i in range(n)]
    t = [input() for i in range(m)]
    ans = 0
    for si in s:
        ans += si in t
    print(ans)
    