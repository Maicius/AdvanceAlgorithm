import sys
from copy import deepcopy
import itertools

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

    order = [x for x in range(num_people)]
    all_order = get_all_order(order)
    final_result = {}

    for item in all_order:
        sum_val = 0
        for i in range(len(item)):
            sum_val += data_matrix[i][item[i]]

        if sum_val not in final_result:
            final_result[sum_val] = [list(item)]
        else:
            index = compare_item(final_result[sum_val], item)
            if index:
                final_result[sum_val].append(list(item))
            else:
                final_result[sum_val].insert(0, list(item))

    min_val = min(list(final_result.keys()))
    best = final_result[min_val]
    result = []
    for item in best:
        item = list(map(lambda x: str(x + 1), item))
        str_val = " ".join(item)
        result.append(str_val)
    print(",".join(result))
    pass

def compare_item(node, node1):
    for i in range(len(node[0])):
        if node[0][i] > node1[i]:
            return True
        elif node[0][i] < node1[i]:
            return False

def get_all_order(list1):
    return list(itertools.permutations(list1,len(list1)))

if __name__ =='__main__':
    get_input()