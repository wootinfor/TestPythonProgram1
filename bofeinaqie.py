def hanoi(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi(n - 1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n - 1, b, a, c)


# 调用
hanoi(5, 'A', 'B', 'C')


# def px(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return px(n-1)*n


# print(px(5))

def hannuota(n):
    if n == 1:
        return 1
    else:
        return hannuota(n-1)+hannuota(1)+hannuota(n-1)


print(hannuota(7))
