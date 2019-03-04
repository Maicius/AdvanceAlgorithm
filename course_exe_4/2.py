import sys


def get_input():
    file = open('2.txt', 'r')
    sys.stdin = file
    testcase = int(input().strip())
    for i in range(testcase):
        num = int(input().strip())
        line = input().strip()
        arr = line.split(' ')
        arr = list(map(int, arr))
        print(calculate(arr))

def calculate(arr):
    arr = sorted(arr)
    sum1 = sum(arr)
    arr.pop(0)
    sum2 = sum(arr)
    return sum2 if sum2 > sum1 else sum1

if __name__ == '__main__':
    get_input()