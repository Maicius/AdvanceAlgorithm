import sys


def get_input():
    sys.stdin = open('../course_exe_3/4.txt', 'r')
    test_case = int(input().strip())
    for i in range(test_case):
        line = input().strip()
        text = line.split(',')[0]
        sub = line.split(',')[1]
        calculate(text, sub)

def calculate(text, sub):
    index_list = []
    text_len = len(text)
    for i in range(text_len):
        is_match = True
        if text[i] == sub[0]:
            for j in range(len(sub)):
                try:
                    if text[i + j] != sub[j]:
                        is_match = False
                        break
                except:
                    is_match = False
                    break
            if is_match:
                index_list.append(str(i))
    print(" ".join(index_list))

if __name__ == '__main__':
    get_input()