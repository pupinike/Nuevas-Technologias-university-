def serie(n):
    a = 5
    b = 8
    for k in range (n):
        c = a+b ##13        
        a = b ##8   
        b = c ##13+8
    return b


for x  in range(100):
     print(serie(x))

