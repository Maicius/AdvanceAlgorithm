import sys
from copy import deepcopy


class DecreaseQueue(object):
    """
    单调队列
    """
    def __init__(self):
        self.arr, self.win = self.get_input()
        self.queue = []
        self.max_arr = []
    def get_input(self):
        file = open('3.txt', 'r')
        sys.stdin = file
        line = input().strip().split(' ')
        arr = list(map(lambda x: int(x), line))
        win = int(input().strip())
        return arr, win

    def insert_queue(self, queue, value, i):
        width = len(queue)
        index = 0
        if width > 0:
            while index < width and self.queue[index][0] > value:
                index += 1
            self.queue.insert(index, (value, i))
        else:
            self.queue.append((value, i))


    def calculate(self):
        for i in range(len(self.arr)):
            if i < self.win - 1:
                self.insert_queue(self.queue, self.arr[i], i)
            else:
                self.insert_queue(self.queue, self.arr[i], i)
                self.max_arr.append(self.queue[0][0])
                self.queue = list(filter(lambda x: x[1] > i - self.win + 1, self.queue))

        print(sum(self.max_arr))

if __name__ == '__main__':
    dq = DecreaseQueue()
    dq.calculate()

