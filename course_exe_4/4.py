import sys

def getminnum(arr, flag1, flag2):
    if flag1 == len(arr):
        return 0
    sumlist = []
    for i in range(len(arr[flag1])):
        if i != flag2:
            ysum = arr[flag1][i] + getminnum(arr, flag1+1, i)
            sumlist.append(ysum)
    return min(sumlist)

# file = open('4.txt', 'r')
# sys.stdin = file
testcase = int(input().strip())
for i in range(testcase):
    j = int(input().strip())
    arr = []
    for k in range(j):
        arri = list(map(lambda z: int(z), input().strip().split(' ')))
        arr.append(arri)
    print(getminnum(arr, 0, -1))