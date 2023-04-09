if __name__ == '__main__':
    s = input()
    if len(s) == 8:
        if s.count('K') == s.count('Q') == 1 and s.count('R') == s.count('B') == s.count('N') == 2:
            x_B = s.index('B', 0) + 1
            y_B = s.index('B', x_B) + 1
            x_R = s.index('R', 0) + 1
            y_R = s.index('R', x_R) + 1 
            if (x_B + y_B) % 2 == 1 and x_R < s.index('K') + 1 < y_R:
                print('Yes')
            else:
                print("No")
