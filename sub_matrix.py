import sys
from copy import deepcopy

def get_input():
    file = open('input.txt', 'r')
    sys.stdin = file
    matrix = []
    try:
        while True:
            line = input().strip().split(' ')
            arr = list(map(lambda x: int(x), line))
            matrix.append(arr)
    except EOFError:
        pass
    return matrix

def get_max_matrix():
    matrix = get_input()
    matrix.insert(0, [0] * len(matrix[0]))
    get_histogram(matrix)

def calculate_histogram(matrix_i, col):
    ans = 0
    stack =[]
    height = deepcopy(matrix_i)
    height.append(-100000)
    for k in range(0, col + 1):
        if len(stack) == 0 or height[k] >= height[stack[-1]]:
            stack.append(k)
        else:
            while(len(stack) != 0 and height[k] < height[stack[-1]]):
                top = stack[-1]
                stack.pop()
                temp = (k - top) * height[top]
                ans = max(temp, ans)
                # print(ans)
            stack.append(top)
            height[top] = height[k]
    return ans

def get_histogram(matrix):
    row = len(matrix)
    col = len(matrix[0])
    ans = 0
    for i in range(1, row):
        for j in range(col):
            matrix[i][j] = (matrix[i-1][j] + 1) if matrix[i][j] == 1 else 0
        # print(matrix[i])
        res = calculate_histogram(matrix[i], col)
        ans = max(res, ans)
    print(ans)
    return matrix

if __name__ =='__main__':
    get_max_matrix()