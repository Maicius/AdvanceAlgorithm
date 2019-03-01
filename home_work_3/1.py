import sys
from copy import deepcopy
import pandas as pd

def get_input():
    file = open('1.txt', 'r')
    sys.stdin = file
    num_case = int(input().strip())
    for i in range(num_case):
        num_people = int(input().strip())
        line1 = input().strip().split(',')
        data = list(map(lambda x:x.split(' '), line1))
        data = list(map(lambda x: tuple(map(lambda y:int(y), x)), data))
        data = list(sorted(data, key=lambda x:x[0]))
        calculate(data, num_people)
def calculate(data, num_people):
    data_line = [0] * num_people
    data_matrix = []
    for i in range(num_people):
        data_matrix.append(deepcopy(data_line))
    for item in data:
        # people
        i = item[0] - 1
        # task
        j = item[1] - 1
        data_matrix[i][j] = item[2]

    col_label = { x:x + 1 for x in range(num_people)}
    row_label = {x:x + 1 for x in range(num_people)}
    result_list = []
    while row_label:
        row, col, max_row = find_best_mapping(data_matrix, 0)
        result_list.append([row_label[row], col_label[col]])
        col_label.pop(col)
        row_label.pop(row)
        refresh_label(row_label, row)
        refresh_label(col_label, col)

    result_list = sorted(result_list, key=lambda x:x[0])
    result_list = map(lambda x: str(x[1]), result_list)
    print(" ".join(result_list))

def find_all_index(arr,item):
    return [i for i,a in enumerate(arr) if a==item]

def refresh_label(row_label, row):
    temp_dict = deepcopy(row_label)
    for index, value in temp_dict.items():
        if index > row:
            row_label.pop(index)
            index -= 1
        row_label[index] = value

def find_best_mapping(data_martix, row):
    column_data = data_martix[row]
    max_col = min(column_data)
    max_col_index = max(find_all_index(column_data, max_col))
    row_data = list(map(lambda x:x[max_col_index], data_martix))
    max_row = min(row_data)
    # max_row_index = row_data.index(max_row)
    max_row_index = max(find_all_index(row_data, max_row))
    if max_row_index == row:
        data_martix.pop(max_row_index)
        if len(data_martix) > 0:
            for i in range(len(data_martix)):
                data_martix[i].pop(max_col_index)
        return (max_row_index, max_col_index, max_row)
    else:
        return find_best_mapping(data_martix=data_martix, row=max_row_index)


if __name__ =='__main__':
    get_input()
