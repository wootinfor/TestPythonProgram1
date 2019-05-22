sum = 0
for x in range(10000):
    x1=x+1
    x2=x1//2
    for i in range(x2):
        i1=i+1
        a=x1%i1
        if a==0:
            sum =sum+i1
    if sum==x1:
        print(x1)        
