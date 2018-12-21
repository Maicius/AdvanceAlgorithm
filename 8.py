import sys


def get_input():
    sys.stdin = open('8.txt', 'r')
    line = input().strip().split(' ')
    arr = list(map(lambda x: int(x), line))
    line = input().strip().split(' ')
    arr2 = list(map(lambda x: int(x), line))
    return arr, arr2


def calculate(a, b):
    min = abs(sum(a) - sum(b))
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] != b[j]:
                a[i], b[j] = b[j], a[i]
                tmp = abs(sum(a) - sum(b))
                if min > tmp:
                    min = tmp
                else:
                    a[i], b[j] = b[j], a[i]
    return a, b


if __name__ == '__main__':
    arr, arr1 = get_input()
    arr2, arr3 = calculate(arr, arr1)
    # print(arr2, arr3)
    print(abs(sum(arr2) - sum(arr3)))
