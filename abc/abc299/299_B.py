if __name__ == "__main__":
    n, t = map(int, input().split())
    c = list(map(int, input().split()))
    r = list(map(int, input().split()))
    score = 0
    winner = 0

    if t in c:
        for i in range(n):
            if c[i] == t:
                if r[i] > score:
                    score = r[i]
                    winner = i+1
    else:
        score = r[0]
        winner = 1
        for j in range(n):
            if c[j] == c[0] and r[j] > score:
                score = r[j]
                winner = j + 1    
    print(winner)