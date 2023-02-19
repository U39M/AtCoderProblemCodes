if __name__ == "__main__":
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result = 0

    for i in range(1, N + 1):
        if i in B:
            result += A[i-1]
    
    print(result)
    