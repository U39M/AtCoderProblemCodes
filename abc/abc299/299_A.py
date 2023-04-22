def Check_String(s):
    front = s.find('|')
    back = s.find('|',front+1)
    asterisk = s.find('*', front+1, back) 
    ans = "out" if asterisk < 0 else "in"
    return ans

if __name__ == "__main__":
    n = int(input())
    s = input()
    print(Check_String(s))