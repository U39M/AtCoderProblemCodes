if __name__ == "__main__":
    N = int(input())
    W = list(map(str, input().split()))
    ans = ['and', 'not', 'that', 'the', 'you']

    for _ in range(len(W)):
        if W[_] in ans:
            print("Yes")
            exit()
    
    print("No")
