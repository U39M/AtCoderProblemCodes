# Aを90度回転する関数
def rotate(A, N):
    return [[A[N-1-j][i] for j in range(N)] for i in range(N)]

# BがAを回転させたものであるかを判定する関数
def check(A, B, N):
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1:
                if B[i][j] != 1:
                    return False
    return True

def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    B = [list(map(int, input().split())) for _ in range(N)]
    # 回転してBと一致するかを調べる
    for _ in range(4):
        if check(A, B, N):
            print("Yes")
            exit()
        A = rotate(A, N)
    print("No")

if __name__ == '__main__':
    main()