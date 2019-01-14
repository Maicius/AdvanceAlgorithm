import sys

def get_input():
    sys.stdin = open('../course_exe_3/3.txt', 'r')
    test_case = int(input().strip())
    for i in range(test_case):
        n = int(input().strip())
        calculate(n)

def calculate(n):
    arr = '12345'
    count = 1
    while len(arr) < n:
        arr = arr + "$" * count + arr[::-1]
        count += 1

    print(arr[n - 1])

if __name__ =='__main__':
    get_input()