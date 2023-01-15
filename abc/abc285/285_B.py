N = int(input())
S = input()

for i in range(1, N):
  flag = True
  for k in range(N-i):
    if S[k] == S[k+i]:
      print(k)
      flag = False
      break
  if flag:
    print(N-i)
