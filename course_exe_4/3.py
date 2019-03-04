import sys

def get_input():
    file = open('3.txt', 'r')
    sys.stdin = file

    num_case = int(input().strip())

    for i in range(num_case):
        num = int(input().strip())
        arr = input().strip().split(' ')
        arr = list(map(int, arr))
        print(calculate(arr, num))

def calculate(arr, num):
    if num == 1:
        return arr[0]
    else:
        val = arr.pop()
        if val - 1 in arr:
            arr.remove(val - 1)
        if len(arr) > 0:
            return val + calculate(arr, len(arr))
        else:
            return val


if __name__ == '__main__':
    get_input()