def mikic(x, *args):
    m = x
    n = 0
    s = 0
    if (x == -1):
        if (n == 0):
            s = x
            a = x
            
            print (n,s,a,m)
    else:
        s = s + x
        n = n + 1 
        a = s / n
        for arg in args:
            if (arg != -1):
                i = arg
                s = s + i
                n = n + 1
                a = s / n
                if (i <= m):
                    m = i
                    
        print (n,s,a,m) 
        
        
            

mikic(3,4,0,2,1,8,-1)
mikic(5,2,3,4,0,-1)
mikic(-1)