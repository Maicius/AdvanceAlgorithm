import sys
def get_input():
    sys.stdin = open('7.txt', 'r')
    line = input().strip().split(' ')
    arr = list(map(lambda x: int(x), line))

    return arr

def calculate(arr):
    """
    二分法 + 动态规划
    :param arr:
    :return:
    """
    increase = [-1000] * len(arr)
    max = 0
    increase[0] = arr[0]
    # 保存路径
    route = {}
    route[arr[0]] = [arr[0]]
    for i in range(1, len(arr)):
        left = 0
        right = max
        while left <= right:
            mid = (left + right) // 2
            if increase[mid] < arr[i]:
                left = mid + 1
            else:
                right = mid - 1
        increase[left] = arr[i]
        if left > max:
            max += 1

        if increase[left - 1] in route:
            route[arr[i]] = route[increase[left - 1]] + [arr[i]]
        else:
            route[arr[i]] = [arr[i]]

    return increase, max, route

if __name__ =='__main__':
    arr = get_input()
    arr1, max, route = calculate(arr)
    arr.reverse()
    arr2, max2, route2 = calculate(arr)
    i = 0
    for i in range(len(arr)):
        if arr1[i] + arr2[i] > max:
            max = i + i + 2
    # print(len(arr) - max + 1)
    index = (max - 2) // 2
    best_value = arr1[index] if arr1[index] > arr2[index] else arr2[index]
    # print(best_value)
    route2[best_value].reverse()
    res = list(map(str, route[best_value] + route2[best_value][1:]))
    print(" ".join(res))

