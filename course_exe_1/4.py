import sys

file = open('../course_exe_1/4.txt', 'r')
sys.stdin = file
num_test = int(input().strip())

class Merge_sort(object):
    def __init__(self):
        self.count = 0
    def get_input(self):
        num = int(input().strip())
        line = input().strip().split(' ')
        arr = list(map(lambda x: int(x), line))
        return num, arr

    def merge(self, a, b):
        c = []
        h = j = 0
        while j < len(a) and h < len(b):
            if a[j] < b[h]:
                c.append(a[j])
                j += 1
            else:
                c.append(b[h])
                h += 1
                self.count += len(a) - j
        if j == len(a):
            for i in b[h:]:
                c.append(i)
        else:
            for i in a[j:]:
                c.append(i)
        return c

    def merge_sort(self, lists):
        if len(lists) <= 1:
            return lists
        middle = len(lists) // 2
        left = self.merge_sort(lists[:middle])
        right = self.merge_sort(lists[middle:])
        return self.merge(left, right)

if __name__ =='__main__':
    for i in range(num_test):
        ms = Merge_sort()
        num, arr = ms.get_input()
        ms.merge_sort(arr)
        print(ms.count)