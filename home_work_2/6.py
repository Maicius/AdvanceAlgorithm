import sys

def get_input():
    file = open('6.txt', 'r')
    sys.stdin = file
    while True:
        try:
            line1 = input().strip().split(' ')
            arr = list(map(int, line1))
            # bubbleSort(arr[1:])
            quick_sort(arr[1:])
        except EOFError:
            exit()


def quick_sort(arr):
    '''''
    模拟栈操作实现非递归的快速排序
    '''
    if len(arr) < 2:
        return arr
    stack = []
    stack.append(len(arr)-1)
    stack.append(0)
    while stack:
        l = stack.pop()
        r = stack.pop()
        index = partition(arr, l, r)
        if l < index - 1:
            stack.append(index - 1)
            stack.append(l)
        if r > index + 1:
            stack.append(r)
            stack.append(index + 1)
    arr = list(map(str, arr))
    print(" ".join(arr))

def partition(arr, start, end):
    pivot = arr[start]
    while start < end:
        while start < end and arr[end] >= pivot:
            end -= 1
        arr[start] = arr[end]
        while start < end and arr[start] <= pivot:
            start += 1
        arr[end] = arr[start]
    arr[start] = pivot
    return start

if __name__ == '__main__':
    get_input()