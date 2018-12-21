import sys
file = open('../course_exe/3.txt', 'r')
sys.stdin = file

def sort(A1, A2):
    listx = []
    temp = []
    res = []
    for i in range(len(A2)+1):
        listx.append(temp[:])
    for i in A1:
        find = False
        for j in range(len(A2)):
            if i == A2[j]:
                listx[j].append(i)
                find = True
                break
        if not find:
            listx[len(A2)].append(i)
    for i in range(0, len(listx)-1):
        res.extend(listx[i])
    lasr = sorted(listx[len(listx)-1])
    res.extend(lasr)
    return res


testcase = int(input().strip())
for i in range(testcase):
    line = input().strip()
    flength = int(line.split(' ')[0])
    slength = int(line.split(' ')[1])
    a1 = list(map(lambda x: int(x), input().strip().split(' ')))
    a2 = list(map(lambda x: int(x), input().strip().split(' ')))
    res = sort(a1, a2)
    res = list(map(lambda x: str(x), res))
    print(" ".join(res))