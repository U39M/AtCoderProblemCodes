if __name__ == "__main__":
    N, K = map(int, input().split())
    S = []
    ans = []

    for i in range(N):
        S.append(input())
    
    for j in range(K):
        ans.append(S[j])
    
    ans.sort()

    for k in range(K):
        print(ans[k])
        

