import sys
file = open('../course_exe_1/4.txt', 'r')
sys.stdin = file

num_test = int(input().strip())
def get_input():
    num = int(input().strip())
    line = input().strip().split(' ')
    arr = list(map(lambda x: int(x), line))
    return num, arr

def min_swaps(arr):
    n = len(arr)
    arr_index = [*enumerate(arr)]
    arr_index.sort(key=lambda it: it[1])
    vis = {k: False for k in range(n)}
    ans = 0
    for i in range(n):
        if vis[i] or arr_index[i][0] == i:
            continue
        cycle_size = 0
        j = i
        while not vis[j]:
            vis[j] = True
            j = arr_index[j][0]
            cycle_size += 1
        if cycle_size > 0:
            ans += (cycle_size - 1)
    return ans

for i in range(num_test):
    num, arr = get_input()
    print(min_swaps(arr))