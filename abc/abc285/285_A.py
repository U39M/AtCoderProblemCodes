def check(a, b):
    flag = False
    
    a_left = 2 * a
    a_right = a_left + 1

    if b == a_left or b == a_right:
        flag = True

    return flag

if __name__ == "__main__" :
    a,b = map(int, input().split())
    if 1 <= a < b <= 15:
        if check(a, b) == True:
            print("Yes")
        else:
            print("No")
