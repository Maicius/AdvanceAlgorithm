import sys

def maxrupees(n, x, y, arr1, arr2):
    if n == len(arr1):
        return 0
    if x == 0:
        ysum = 0
        for i in range(n, len(arr2)):
            ysum = ysum + arr2[i]
        return ysum
    if y == 0:
        xsum = 0
        for i in range(n, len(arr1)):
            xsum = xsum + arr1[i]
        return xsum
    return max(arr1[n] + maxrupees(n+1, x-1, y, arr1, arr2), arr2[n] + maxrupees(n+1, x, y-1, arr1, arr2))

def get_input():
    file = open('1.txt', 'r')
    sys.stdin = file
    testcase = int(input().strip())
    for i in range(testcase):
        line = input().strip()
        x = int(line.split(" ")[1])
        y = int(line.split(' ')[2])
        arr1 = list(map(lambda z: int(z), input().strip().split(' ')))
        arr2 = list(map(lambda z: int(z), input().strip().split(' ')))
        print(maxrupees(0, x, y, arr1, arr2))

if __name__ == '__main__':
    get_input()