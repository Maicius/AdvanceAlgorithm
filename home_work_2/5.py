import sys

def get_input():
    file = open('4.txt', 'r')
    sys.stdin = file
    while True:
        try:
            line1 = input().strip().split(' ')
            arr = list(map(int, line1))
            bubbleSort(arr[1:])
        except EOFError:
            exit()

def bubbleSort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 2, i - 1, -1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    nums = list(map(str, nums))
    print(" ".join(nums))


if __name__ =='__main__':
    get_input()