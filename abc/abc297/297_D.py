A, B = map(int, input().split())
ans = 0

# 入力値が同値である場合、0回を出力
if A == B:
    print(0)
    exit()

while(A!=B):
    if A == 0 or B == 0:
        print(ans - 1)
        exit() 
    if A < B:
        A, B = B, A
    if A > B:
        ans += A//B
        A = A % B
    

print(ans -1)
