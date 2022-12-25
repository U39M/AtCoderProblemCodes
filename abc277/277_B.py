# coding: utf-8
# Your code here!
n = int(input())
s = []


def check1(l):
    headChar = {'H', 'D', 'C', 'S'}
    flag = False

    for i in range(n):
        if l[i][0:1] in headChar:
            flag = True
        else:
            flag = False
            break

    return flag


def check2(l):
    secChar = {'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'}
    flag = False

    for i in range(n):
        if l[i][1:2] in secChar:
            flag = True
        else:
            flag = False
            break

    return flag


def check3(l):
    flag = True
    for i in range(0, n-1):
       for j in range(i+1, n):
           if l[j] == l[i]:
               flag = False
    return flag


def main():
    if 1 < n <= 52:
        for i in range(n):
            s.append(input())

        if check1(s) == check2(s) == check3(s) == True:
            print("Yes")
        else:
            print("No")


main()
