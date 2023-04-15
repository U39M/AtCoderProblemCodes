def Check_Interview(n, s):
    good_in_s = "o" in s
    falling_not_in_s = "x" not in s

    if good_in_s == falling_not_in_s == True:
        return "Yes"
    return "No"

def main():
    n = int(input())
    s = input()
    print(Check_Interview(n, s))
    return

if __name__ == '__main__':
    main()