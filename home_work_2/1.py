import sys

l1_dp = {}
l2_dp = {}

ans = []

def get_input():
    file = open('1.txt', 'r')
    sys.stdin = file
    line1 = input().strip()
    line2 = input().strip()
    return line1, line2


def max_len(arr1, arr2):
    global ans
    if len(arr2) != len(arr1):
        return arr1 if len(arr1) > len(arr2) else arr2
    elif arr1.strip() != '':
        if arr1 == arr2:
            return arr1
        else:
            return arr1 + ';' + arr2

    else:
        return arr2


def calculate(l1, l2):
    m = len(l1) - 1
    n = len(l2) - 1

    global l1_dp

    if str(m) + str(n) in l1_dp:
        return l1_dp[str(m) + str(n)]

    if m < 0 or n < 0:
        return ''

    elif l1[m] == l2[n]:
        temp = calculate(l1[:m], l2[: n]) + l1[m]
        l1_dp[str(m) + str(n)] = temp
        return temp

    else:
        temp1 = calculate(l1[:m], l2[:n + 1])
        temp2 = calculate(l1[:m + 1], l2[:n])
        temp = max_len(temp1, temp2)

        l1_dp[str(m) + str(n)] = temp
        return temp


if __name__ == '__main__':
    l1, l2 = get_input()
    res = calculate(l1, l2)
    if res.find(';') == -1:
        print(res)
    else:
        index = res.find(';')
        arr = res.split(';')
        longest = list(filter(lambda x: len(x) > index, arr))[0]
        arr.remove(longest)
        for item in arr:
            print(item + str(longest[index:]))
        print(longest)
