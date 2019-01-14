import sys

def get_input():
    sys.stdin = open('../course_exe_3/1.txt', 'r')
    test_case = int(input().strip())
    for i in range(test_case):
        line = input().strip()
        calculate(line)

def calculate(line):
    res = []
    length = len(line)
    for i in range(length - 1, -1, -1):
        for j in range(i - 1, -1, -2):
            right = 0
            left = 0
            for k in range(j, i + 1):
                if k > (i + j) / 2:
                    right += int(line[k])
                else:
                    left += int(line[k])
            if right == left and (i - j + 1) % 2 == 0:
                res.append(i - j + 1)
    if len(res) > 0:

        print(max(res))
    else:
        print(0)

if __name__ =='__main__':
    get_input()
