def binary_search(array, value):
    """
    二分查找
    :param array: 有序数组
    :param value: 查找的值
    :return: 找到返回索引，否则返回-1
    """
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == value:
            return mid
        elif array[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_recursion(array, value, left=0, right=None):
    """
    递归实现二分查找
    :param array: 有序数组
    :param value: 查找的值
    :param left: 左边界
    :param right: 右边界
    :return: 找到返回索引，否则返回-1
    """
    if right is None:
        right = len(array) - 1
    if left <= right:
        mid = (left + right) // 2
        if array[mid] == value:
            return mid
        elif array[mid] < value:
            return binary_search_recursion(array, value, mid + 1, right)
        else:
            return binary_search_recursion(array, value, left, mid - 1)
    return -1


if __name__ == '__main__':
    # array = [-1, 2, 3, 3, 5, 6, 7]
    # index = binary_search(array, 5)
    # print(index)
    array = [-1, 2, 3, 3, 5, 6, 7]
    index = binary_search_recursion(array, 5)
    print(index)
