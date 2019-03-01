import sys

mark = 0
table = []

def get_input():
    file = open('4.txt', 'r')
    sys.stdin = file
    num_case = int(input().strip())
    for i in range(num_case):
        line1 = input().strip().split(' ')
        data = list(map(lambda x: int(x), line1))
        line2 = input().strip().split(' ')
        data2 = list(map(int, line2))
        calculate(data, data2)
def calculate(data, data2):
    global table
    n = 2 ** data[0]
    table = [[-1 for x in range(n)] for y in range(n)]
    chess(0, 0, data[1], data[2], n)

    point = table[data2[0]][data2[1]]
    show(table, point, data2)

def chess(tr, tc, pr, pc, size):
    global mark
    global table
    mark += 1
    count = mark
    if size == 1:
        return
    half = size // 2
    if pr < tr + half and pc < tc + half:
        chess(tr, tc, pr, pc, half)
    else:
        table[tr + half - 1][tc + half - 1] = count
        chess(tr, tc, tr + half - 1, tc + half - 1, half)
    if pr < tr + half and pc >= tc + half:
        chess(tr, tc + half, pr, pc, half)
    else:
        table[tr + half - 1][tc + half] = count
        chess(tr, tc + half, tr + half - 1, tc + half, half)
    if pr >= tr + half and pc < tc + half:
        chess(tr + half, tc, pr, pc, half)
    else:
        table[tr + half][tc + half - 1] = count
        chess(tr + half, tc, tr + half, tc + half - 1, half)
    if pr >= tr + half and pc >= tc + half:
        chess(tr + half, tc + half, pr, pc, half)
    else:
        table[tr + half][tc + half] = count
        chess(tr + half, tc + half, tr + half, tc + half, half)


def show(table, point, data2):
    n = len(table)
    result = []
    for i in range(n):
        for j in range(n):
            if i == data2[0] and j == data2[1]:
                pass
            elif table[i][j] == point:
                result.append(str(i) +" " + str(j))
    print(",".join(result))


if __name__ =='__main__':
    get_input()
