import sys

def get_input():
    file = open('6.txt', 'r')
    sys.stdin = file
    while True:
        try:
            line1 = input().strip().split(' ')
            arr = list(map(int, line1))
            # bubbleSort(arr[1:])
            merge_sort(arr[1:])
        except EOFError:
            exit()

def merge(seq,low,mid,height):
    left = seq[low:mid]
    right = seq[mid:height]
    k = 0
    j = 0
    result = []
    while k < len(left) and j < len(right):
        if left[k] <= right[j]:
            result.append(left[k])
            k += 1
        else:
            result.append(right[j])
            j += 1
    result += left[k:]
    result += right[j:]
    seq[low:height] = result


def merge_sort(seq):
    i = 1
    while i < len(seq):
        low = 0
        while low < len(seq):
            mid = low + i
            height = min(low + 2 * i, len(seq))
            if mid < height:
                merge(seq, low, mid, height)
            low += 2 * i
        i *= 2

    seq = list(map(str, seq))
    print(" ".join(seq))

if __name__ =='__main__':
    get_input()