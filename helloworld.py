print('hello world')
for x in list(range(900)):
    x=x+100
    y=[int(i) for i in str(x)]
    h=y[1]*y[1]*y[1]+y[2]*y[2]*y[2]+y[0]*y[0]*y[0]
    if x==h:
        print(h)