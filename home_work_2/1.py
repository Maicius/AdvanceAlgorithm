import sys

l1_dp = {}
l2_dp = {}
def get_input():
    file = open('1.txt', 'r')
    sys.stdin = file
    line1 = input().strip()
    line2 = input().strip()
    return line1, line2

def max_len(arr1, arr2):
    if len(arr2) != len(arr1):
        return arr1 if len(arr1) > len(arr2) else arr2
    else:
        return arr2

def calculate(l1, l2):
    m = len(l1) - 1
    n = len(l2) - 1
    global l2_dp
    global l1_dp

    if n in l2_dp:
        return l2_dp[n]
    if m in l1_dp:
        return l1_dp[m]

    if m < 0 or n < 0:
        return ''

    elif l1[m] == l2[n]:
        temp = calculate(l1[:m], l2[: n]) + l1[m]
        l1_dp[m] = temp
        l2_dp[n] = temp
        return temp

    else:
        temp1 = calculate(l1[:m], l2[:n + 1])
        temp2 = calculate(l1[:m + 1], l2[:n])

        return max_len(calculate(l1[:m], l2[:n + 1]),
                   calculate(l1[:m + 1], l2[:n]))



if __name__ == '__main__':
    l1, l2 = get_input()

    print(calculate(l1, l2))