import sys
from copy import deepcopy
from functools import cmp_to_key


def get_input():
    file = open('../course_exe/1.txt', 'r')
    sys.stdin = file
    num_test = int(input().strip())
    
    num = int(input().strip())
    line = input().strip().split(' ')
    arr = list(map(lambda x: int(x), line))
    return num_test, num, arr


def calculate():
    res = {}
    num_test, num, arr = get_input()
    for i in range(num_test):
        for item in arr:
            if item not in res:
                res[item] = 1
            else:
                res[item] += 1
        sort_res = list(sorted(res.items(), key=cmp_to_key(lambda x, y: sort_dict(x, y))))
        # print(sort_res)
        format_output(sort_res)


def sort_dict(x, y):
    if x[1] == y[1]:
        return 1 if x[0] > y[0] else -1
    else:
        return 1 if x[1] < y[1] else -1

def format_output(data):
    res = []
    for i in range(len(data)):
        for j in range(data[i][1]):
            res.append(str(data[i][0]))
    print(" ".join(res))

if __name__ == '__main__':
    calculate()
