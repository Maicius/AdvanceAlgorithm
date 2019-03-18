import sys
from copy import deepcopy

def get_input():
    file = open('3.txt', 'r')
    sys.stdin = file
    num_case = int(input().strip())
    for i in range(num_case):
        num = int(input().strip())
        line1 = input().strip().split(' ')
        data = list(map(int, line1))

        calculate(data, num)

def calculate(data, num):

    data_line = [0] * num
    data_matrix = []
    for i in range(num):
        data_matrix.append(deepcopy(data_line))
    for i in range(1, len(data) - 1, 3):
        data_matrix[data[i - 1] - 1][data[i] - 1] = data[i + 1]

    for i in range(num):
        max_time = max(data_matrix[i])
        index = data_matrix[i].index(max_time)

        for j in range(num):
            if data_matrix[i][j] < max_time and j < index:
                data_matrix[i][j] = max_time

    new_data = []
    for i in range(num):
        line = list(map(lambda x: x[i], data_matrix))
        new_data.append(line)

    sum_val = 0
    i = 0
    count = 0
    while new_data:

        max_item = max(new_data[i])
        index = new_data[i].index(max_item)
        new_data.remove(new_data[i])
        new_data = remove_index(index, new_data)
        if max_item > 0:
            sum_val += max_item
            count += 1
    print(count, sum_val)

def remove_index(index, data):
    for i in range(len(data)):
        for j in range(len(data[0])):
            if j == index:
                data[i][j] = 0

    return data

if __name__ == '__main__':
    get_input()