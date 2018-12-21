import sys

def get_input():
    file = open('5.txt', 'r')
    sys.stdin = file
    line = input().strip().split(' ')
    arr = list(map(lambda x: int(x), line))
    line = input().strip().split(' ')
    width = list(map(lambda x: int(x), line))
    k = int(input().strip())
    return arr, width, k

if __name__ =='__main__':
    arr, width, k = get_input()
    arr = list(sorted(arr[width[0] - 1: width[1]]))
    print(arr[k - 1])
