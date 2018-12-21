import sys
file = open('../course_exe_1/4.txt', 'r')
sys.stdin = file

count = 0


def merge(a, b):
    global count
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1
            count += (len(a) - j)

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)

    return c


def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = int(len(lists)/2)
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)


casenum = int(input())
tempnum = casenum
paraarr = []
while casenum > 0:
    input()
    paraarr.append(input())
    casenum -= 1
for i in range(0, tempnum):
    arr = paraarr[i].split(' ')
    count = 0
    merge_sort(arr)
    print(count)