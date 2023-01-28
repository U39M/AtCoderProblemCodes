if __name__ == "__main__":
    n,a,b = map(int,input().split())
    s = list(input()) * 2

    ret = 10 ** 18
    for i in range(n):
        ans = a * i * 2
        for j in range(n):
            if s[i + j] != s[i + n - 1 - j]:
                ans += b
        ret = min(ret, ans // 2)
        #print(ans // 2)
    print(ret)

