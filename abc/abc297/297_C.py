if __name__ == '__main__':
    # 入力を受け取る
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    # 右隣と同じ文字の箇所を操作する
    for i in range(H):
        for j in range(W-1):
            if S[i][j] == S[i][j+1] == 'T':
                S[i][j] = 'P'
                S[i][j+1] = 'C'

    # 操作後の文字列を出力
    for i in range(H):
        print(''.join(S[i]))
