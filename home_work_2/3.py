import sys

def get_input():
    file = open('3.txt', 'r')
    sys.stdin = file
    while True:
        try:
            line1 = input().strip().split(' ')
            calculate(line1)
        except EOFError:
            exit()

def calculate(arr):
    num = int(arr[0])
    k = int(arr[-1])
    arr = arr[1:-1]
    res = []
    i = 0
    for i in range(0, num - k + 1, k):
        temp = arr[i: i + k]
        temp.reverse()
        res.extend(temp)
    if num % k != 0:
        res.extend(arr[-k + 1:])
    print(" ".join(res))

if __name__ =='__main__':
    get_input()
