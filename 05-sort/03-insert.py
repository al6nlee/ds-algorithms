"""
插入排序
"""


def insert_sort(alist):
    n = len(alist)
    for i in range(1, n):
        temp = alist[i]
        j = i
        while j > 0 and temp < alist[j - 1]:
            alist[j] = alist[j - 1]
            j -= 1
        alist[j] = temp
    return alist


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(insert_sort(alist))
