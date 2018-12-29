import sys

def get_input():
    sys.stdin = open('../course_exe_2/3.txt', 'r')
    num_test = int(input().strip())
    for i in range(num_test):
        line = list(map(int, input().strip().split(' ')))
        k = line[0]
        n = line[1]
        boards = list(map(int, input().strip().split(' ')))
        print(calculate(k, n, boards))

def calculate(k, n, boards):
    dp = []
    for i in range(k + 1):
        dp.append([0] * (n + 1))

    # k = 1
    for i in range(1, n + 1, 1):
        temp_arr = boards[0: i]
        dp[1][i] = sum(temp_arr)

    # n = 1
    for i in range(1, k + 1, 1):
        dp[i][1] = boards[0]

    for i in range(2, k+ 1, 1):
        for j in range(2, n+ 1, 1):
            best = 9999999
            for p in range(1, j + 1, 1):
                temp = boards[p: j]
                best = min(best, max(dp[i - 1][p], sum(temp)))
            dp[i][j] = best

    return dp[k][n]

if __name__ =='__main__':
    get_input()