def num_pass(n,k,s):
    t = ""

    for i in range(n):
        if k > 0:
            if s[i] == 'o':
                t += 'o'
                k -= 1
            else:
                t += 'x'
        else:
            t += 'x'
    print(t)




if __name__ == "__main__":
    N, K = map(int, input().split())
    S = input()

    if len(S) == N:
        num_pass(N, K, S)
    else:
        exit()
    