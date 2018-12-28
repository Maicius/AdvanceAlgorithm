import sys
from functools import cmp_to_key

class ConvexHull(object):

    def __init__(self):
        self.p0 = (0, 0)
        self.stack_point = []

    def get_input(self):
        sys.stdin = open('../course_exe_2/2.txt', 'r')
        num_test = int(input().strip())
        try:
            while True:
                num_point = int(input().strip())
                num_list = list(map(int, input().strip().split(" ")))
                self.calculate(num_point, num_list)
                self.p0 = (0, 0)
                self.stack_point = []
        except EOFError:
            exit()

    def sort_point(self, x, y):
        if x[0] == y[0]:
            return 1 if x[1] > y[1] else -1
        else:
            return 1 if x[0] > y[0] else -1

    # 0: colinear
    # 1: clockwise
    # 2: counterclockwise

    def orientation(self, p, q, r):
        distance = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if distance == 0:
            return 0
        return 1 if distance > 0 else 2

    def distance(self, x, y):
        return (y[1] - x[1])**2 + (y[0] - x[0])**2

    def sort_distance(self, x, y):
        d = self.orientation(self.p0, x, y)
        if d == 0:
            return 1 if self.distance(self.p0, x) >= self.distance(self.p0, y) else -1
        return -1 if d == 2 else 1

    def calculate(self, num_point, num_list):
        point_list = []
        for i in range(0, num_point * 2 - 1, 2):
            point = (num_list[i], num_list[i + 1])
            point_list.append(point)

        point_list = list(sorted(point_list, key=cmp_to_key(lambda x, y: self.sort_point(x, y))))
        # print(point_list)
        p0 = point_list[0]
        self.p0 = p0
        # print('p0', p0)
        point_list1 = point_list[1:]
        point_list1 = list(sorted(point_list1, key=cmp_to_key(lambda x, y: self.sort_distance(x, y))))
        # print(point_list1)
        new_point_list = []
        for i in range(len(point_list1)):
            while i < len(point_list1) - 1 and self.orientation(self.p0, point_list1[i], point_list1[i + 1]) == 0:
                i += 1
            new_point_list.append(point_list1[i])
        new_point_list.insert(0, self.p0)
        # print(new_point_list)
        m = len(new_point_list)
        if m < 3:
            print(-1)
            return
        self.stack_point.append(new_point_list[0])
        self.stack_point.append(new_point_list[1])
        self.stack_point.append(new_point_list[2])

        for i in range(3, m, 1):
            while self.orientation(self.next_to_top(), self.stack_point[-1], new_point_list[i]) != 2:
                self.stack_point.pop()
            self.stack_point.append(new_point_list[i])

        self.stack_point = sorted(self.stack_point, key=lambda x: x[0])

        for i in range(len(self.stack_point) - 1):
            print(self.stack_point[i][0], self.stack_point[i][1], end=', ')
        print(self.stack_point[-1][0], self.stack_point[-1][1])

        # print("stack:", self.stack_point)

    def next_to_top(self):
        p = self.stack_point[-1]
        # print('p', p)
        self.stack_point.pop()
        res = self.stack_point[-1]
        self.stack_point.append(p)
        return res


if __name__ =='__main__':
    ch = ConvexHull()
    ch.get_input()
