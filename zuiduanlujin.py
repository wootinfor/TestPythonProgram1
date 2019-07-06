def zdlj(narr):
    return lujin(len(narr[0])-1, len(narr)-1, narr)


def lujin(i, j, narr):#此方法是求对于二位数组narr中坐标为（i，j）的点的最短路径之和
    print(i, j, narr)
    if j == 0 and i == 0:
        print('narr00', narr[0][0])
        return narr[0][0]
    elif j == 0 and i == 1:
        print('narr0001', narr[0][0]+narr[0][1])
        return narr[0][0]+narr[0][1]
    elif j == 1 and i == 0:
        print('narr0010', narr[0][0]+narr[1][0])
        return narr[0][0]+narr[1][0]
    else:
        if i==0:
           return lujin(i,j-1,narr)+narr[j][i]
        elif j==0:
            return lujin(i-1,j,narr)+narr[j][i]
        else:
            return min(lujin(i-1, j, narr), lujin(i, j-1, narr))+narr[j][i]

def mini_path_sum(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i == 0 and j > 0:
                grid[i][j] += grid[i][j-1]
            elif j == 0 and i > 0:
                grid[i][j] += grid[i-1][j]
            elif i > 0 and j > 0:
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    print(grid)
    return grid[-1][-1]


print('答案1',mini_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))

print('答案2',zdlj([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
