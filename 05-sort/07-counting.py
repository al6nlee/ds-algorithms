def count_sort(array):
    """
    计数排序
    :param array: 待排序数组
    :return: 排序后的数组
    """
    length = len(array)
    max_value = max(array)
    count = [0] * (max_value + 1)
    for i in range(length):
        count[array[i]] += 1  # 将数组中每个元素出现的次数记录到count数组中

    sorted_array_index = 0
    for j in range(max_value + 1):
        while count[j] > 0:
            array[sorted_array_index] = j  # 将统计数组中每个元素出现的次数，依次填充到新数组中
            sorted_array_index += 1
            count[j] -= 1

    return array


if __name__ == '__main__':
    array = [5, 2, 3, 2, 1, 8, 88, 88]
    print(count_sort(array))
