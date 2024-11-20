def seq_search(array, item):
    """
    顺序查找
    :param array: 待查找数组
    :param item: 查找元素
    :return: 查找元素在数组中的索引，若不存在则返回-1
    """
    length = len(array)
    for i in range(length):
        if array[i] == item:
            return i
    return -1


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(seq_search(array, 5))
