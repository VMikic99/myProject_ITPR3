def mikic(n):
    x = n
    y = 0
    i = 1 
    r = 0
    
    
    while (r <= n):
        y = r 
        r = i * i 
        i = i + 1 
        
    print (x,y)
    
mikic(30)
mikic(5)
mikic(1)
mikic(101)
