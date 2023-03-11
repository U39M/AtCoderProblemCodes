if __name__ == "__main__":
    s = list(input())
    swap = ""
    ans = ""
    if len(s) % 2 == 0:
        for i in range(1, len(s), 2):
            swap = s[i]
            s[i] = s[i-1]
            s[i-1] = swap
        print(*s, sep='')
    