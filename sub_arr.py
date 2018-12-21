
if __name__ =='__main__':
    arr = input().strip().split(' ')
    arr = list(map(lambda x: int(x), arr))
    num = int(input().strip())
    count = 0
    total_length = len(arr)
    for i in range(total_length):
        length = total_length - i
        for j in range(i, total_length):
            if abs(arr[j] - arr[i]) > num:
                count += 1
                arr_num = length - 2
                count += 2 ** arr_num -1
                length -= 1
    print(count)
