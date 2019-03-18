import sys

def get_input():
    file = open('1.txt', 'r')
    sys.stdin = file
    num_test = int(input().strip())
    for i in range(num_test):
        line = input().strip().split(' ')
        data_list = []
        for j in range(int(line[1])):
            line1 = input().strip().split(' ')
            data = list(map(int, line1))
            data_list.append(data)
        calculate(data_list)


def calculate(data):
    out_put_list = []


    while data:
        i = 0
        ing = data[i][0]
        out = data[i][1]
        out_put = data[i]
        length = len(data)
        j = 0
        while j < length:

            if data[j][1] == ing:
                out_put[0] = data[j][0]
                out_put[2] = data[j][2] if data[j][2] < out_put[2] else out_put[2]
                data.remove(data[j])
                j = j - 1
            elif data[j][0] == out:
                out_put[1] = data[j][1]
                out_put[2] = data[j][2] if data[j][2] < out_put[2] else out_put[2]
                data.remove(data[j])
                j = j - 1

            for k in range(len(out_put_list)):
                if out_put_list[k][1] == ing:
                    out_put_list[k][0] = out
                    out_put_list[k][2] = data[k][2] if data[k][2] < out_put_list[k][2] else out_put_list[k][2]

                    out_put = []
                    j = j - 1
                    break
                elif out_put_list[i][0] == out:
                    out_put_list[i][0] = ing

                    out_put = []
                    out_put_list[k][2] = data[k][2] if data[k][2] < out_put_list[k][2] else out_put_list[k][2]
                    j = j - 1
                    break

            j += 1
            length = len(data)
        data.remove(data[i])
        if len(out_put) > 0:
            out_put_list.append(out_put)
        # print(out_put_list)
    out_put_list = list(sorted(out_put_list))
    print(len(out_put_list))
    for i in range(len(out_put_list)):
        line = map(str, out_put_list[i])
        print(" ".join(line))
if __name__ == '__main__':
    get_input()