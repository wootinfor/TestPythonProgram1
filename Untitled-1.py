def jiecheng(num):
    factorial = 1 
    # 查看数字是负数，0 或 正数
    if num < 0:
       print("抱歉，负数没有阶乘")
    elif num == 0:
       return(1)
    else:
        for i in range(1,num + 1):
            factorial = factorial*i
    return(factorial)

# print(jiecheng(3))
# print(jiecheng(4))
# print(jiecheng(2))

from functools import reduce
def zhonglei(n):
    sum=0
    m=n//2
    m=int(m)
    # print('m=',m)
    for x in range(0,m+1,1):
        # print('x=',x)
        y=n-2*x
        # print('y=',y)
        s=jiecheng(x+y)/(jiecheng(x)*jiecheng(y))
        # print('s=',int(s))
        sum+=int(s)
    return(sum)

def zhonglei2(m):
    if m==0:
        return 0
    elif m==1:
        return 1
    elif m==2:
        return 2
    else:
        return zhonglei2(m-1)+zhonglei2(m-2)

def zhonglie3(m):
    
    if m==0:
        return 0
    elif m<=2:
        return m
    else:
        i=2
        j=1
        for h in range(3,m+1,1):
            h+=1
            s=i+j
            j=i
            i=s
            print('i=',i)
            print('j=',j)
        return s
            
print(zhonglie3(1234))
