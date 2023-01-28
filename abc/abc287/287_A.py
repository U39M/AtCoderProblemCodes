if __name__ == "__main__" :
    N = int(input())
    S = []

    for_counter = 0
    age_counter = 0

    for i in range(N):
        S.append(input())
        if S[i] == "For":
            for_counter += 1
        else:
            age_counter += 1
    
    if N % 2 != 0:
        if for_counter > age_counter:
            print("Yes")
        else:
            print("No")
    else:
        exit()
