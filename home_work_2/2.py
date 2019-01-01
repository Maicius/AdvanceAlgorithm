import sys

def get_input():
    file = open('2.txt', 'r')
    sys.stdin = file
    while True:
        try:
            line1 = input().strip().split(' ')
            print(calculate(line1))
        except EOFError:
            exit()

def calculate(arr):
    num = int(arr[0])
    arr = arr[1:]
    for i in range(num // 2):
        if arr[i] != arr[num - i - 1]:
            return 'false'
    return 'true'

if __name__ =='__main__':
    get_input()
