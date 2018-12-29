import sys
def findmods(a, b):
    result = []
    mod = a % b
    result.append(mod)
    i = 2
    c = a ** i
    temp = c % b
    while temp != mod:
        result.append(temp)
        i += 1
        c = a ** i
        temp = c % b
    return result


def calculate(a, b, c):
    num = a % c
    result = findmods(num, c)
    mod = b % len(result)
    if mod == 0:
        return result[len(result) -1]
    else:
        return result[mod-1]

def get_input():
    sys.stdin = open('../course_exe_2/1.txt', 'r')
    testcase = int(input().strip())
    for i in range(testcase):
        line = input().strip()
        a = int(line.split(' ')[0])
        b = int(line.split(' ')[1])
        c = int(line.split(' ')[2])
        print(calculate(a, b, c))

if __name__ =='__main__':
    get_input()