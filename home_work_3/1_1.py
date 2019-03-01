import sys
from copy import deepcopy
import pandas as pd

num_people = 0
data_matrix = []
label = []
best = 100000
sum_val = 0

def get_input():
    file = open('1.txt', 'r')
    sys.stdin = file
    num_case = int(input().strip())
    global num_people
    for i in range(num_case):
        global label
        global data_matrix
        global best
        global sum_val
        num_people = 0
        data_matrix = []
        label = []
        best = 100000
        sum_val = 0

        num_people = int(input().strip())
        line1 = input().strip().split(',')
        data = list(map(lambda x:x.split(' '), line1))
        data = list(map(lambda x: tuple(map(lambda y:int(y), x)), data))
        data = list(sorted(data, key=lambda x:x[0]))
        calculate(data, num_people)
def calculate(data, num_people):
    data_line = [0] * num_people
    global data_matrix
    for i in range(num_people):
        data_matrix.append(deepcopy(data_line))
    for item in data:
        # people
        i = item[0] - 1
        # task
        j = item[1] - 1
        data_matrix[i][j] = item[2]
    global label
    for i in range(num_people):
        label.append(i)
    find_best(0)
    print(best)


def find_best(index):
    # print(index)
    print('index', index)

    global best
    global sum_val
    print('sum', sum_val)
    if (index == num_people):
        if sum_val < best:
            best = sum_val
    else:
        for j in range(index, num_people):
            label[j], label[index] = label[index], label[j]

            sum_val += data_matrix[label[index]][index]
            if sum_val <= best:
                find_best(index + 1)

            sum_val -= data_matrix[label[index]][index]
            label[j], label[index] = label[index], label[j]


if __name__ == '__main__':
    get_input()