import sys

def get_input():
    file = open('6.txt', 'r')
    sys.stdin = file
    line = input().strip().split(' ')
    arr = list(map(lambda x: int(x), line))
    num = int(input().strip())
    return arr, num

if __name__ =='__main__':
    arr, num = get_input()
    num_dict = {}
    sum = 0
    for item in arr:
        if item in num_dict:
           sum += 1
        else:
            num_dict[num - item] = 1
    print(sum)