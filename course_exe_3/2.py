import sys

def get_input():
    sys.stdin = open('../course_exe_3/2.txt', 'r')
    test_case = int(input().strip())
    for i in range(test_case):
        line = input().strip()
        line = input().strip().split(' ')
        arr = list(map(int, line))
        line2 = input().strip().split(' ')
        arr2 = list(map(int, line2))
        calculate(arr, arr2)

def calculate(data, div):
    res = []
    for item in div:
        count = 0
        for d in data:
            if d % item == 0:
                count += 1
        res.append(str(count))
    print(" ".join(res))


if __name__ == '__main__':
    get_input()