"""
冒泡排序
"""


def bubble_sort(alist):
    n = len(alist)
    temp = 0  # 临时变量，计算循环了多少圈

    for i in range(n):  # 第一圈，至少会将最大的元素放到最后面。。。所以循环次数为n-1
        flag = False  # 跑一轮下去是否交换过
        for j in range(n - i - 1):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                flag = True
        if not flag:
            break
        temp += 1

    print("循环了%d次" % temp)


if __name__ == '__main__':
    alist = [17, 26, 93, 54, 22]
    bubble_sort(alist)
    print(alist)
