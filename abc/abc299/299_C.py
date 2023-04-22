if __name__ == "__main__":
    n = int(input())
    s = input()
    l = -1
    dango = s.split('-')

    for i in range(len(dango)):
        if len(dango[i]) > l:
            l = len(dango[i])
    
    if l == 0 or '-' not in s:
        l = -1
    print(l)