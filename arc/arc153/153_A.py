if __name__== "__main__" :
    N=int(input())
    for a in range(1,10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        for f in range(10):
                            N-=1
                            if N==0:
                                print(a,a,b,c,d,d,e,f,e,sep='')
                                exit()

