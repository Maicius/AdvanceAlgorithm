import sys


def get_input():
    sys.stdin = open('../course_exe_3/5.txt', 'r')
    test_case = int(input().strip())
    for i in range(test_case):
        N = int(input().strip())
        print(calculate(N))

def calculate(N):
    if N == 2:
        return 2
    elif N == 1:
        return 1
    else:
        return calculate(N - 2) + calculate(N - 1)


if __name__ =='__main__':
    get_input()