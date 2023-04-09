if __name__ == '__main__':
    n, d = map(int, input().split())
    t = list(map(int, input().split()))
    
    for i in range(0, n-1):
        for j in range(i+1, n):
            if t[j] - t[i] <= d:
                print(t[j])
                exit()
    print(-1)