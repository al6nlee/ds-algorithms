def redix_sort(array):
    """
    基数排序
    :param array: 待排序数组
    :return: 排序后的数组
    """
    max_digit = len(str(max(array)))  # 统计数组中最大数的位数
    for i in range(max_digit):
        bucket = [[] for _ in range(10)]  # 创建10个空列表，用于存放待排序的元素
        for num in array:
            bucket[num // (10 ** i) % 10].append(num)  # 将数组中每个元素按照个位、十位、百位……进行分组
        array.clear()  # 清空原数组
        for j in range(10):
            for k in bucket[j]:
                array.append(k)  # 将分组好的元素依次放回原数组中
    return array


if __name__ == '__main__':
    array = [5, 3, 2, 4, 1, 2222, 22]
    print(redix_sort(array))
