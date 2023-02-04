if __name__ == "__main__":
    N = int(input())
    ab = [map(int, input().split()) for _ in range(N)]
    a, b = [list(i) for i in zip(*ab)]

    for j in range(N):
        print(a[j] + b[j])