def swap(l_start, l_end, r_start, r_end, list):
    l_start -= 1

    r_start -= 1
    list[l_start:l_end] , list[r_start:r_end] = list[r_start:r_end] , list[l_start:l_end]
    


    #list[l_start], list[l_end], list[r_start], list[r_end] = list[r_start], list[r_end], list[l_start], list[l_end]

    return list

if __name__ == "__main__" :
    N,P,Q,R,S = list(map(int, input().split()))
    A = list(map(int, input().split()))

    if Q - P == S - R:
        A = swap(P, Q, R, S, A)

    print(*A)
