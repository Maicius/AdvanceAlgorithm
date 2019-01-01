import sys

def get_input():
    file = open('4.txt', 'r')
    sys.stdin = file
    while True:
        try:
            line1 = input().strip().split(' ')
            arr = list(map(int, line1))
            insertSort(arr[1:])
        except EOFError:
            exit()

def insertSort(arr):
    length = len(arr)
    for i in range(length):
        x = arr[i]
        for j in range(i,-1,-1):
            if x < arr[j-1]:
                arr[j] = arr[j-1]
            else:
                break
        arr[j] = x

    arr = list(map(str, arr))
    print(" ".join(arr))


if __name__ =='__main__':
    get_input()
