def bucket_sort(array, bucket_size=10):
    """
    桶排序
    :param array: 待排序数组
    :param bucket_size: 桶的大小，默认为10
    :return: 排序后的数组
    """
    length = len(array)
    max_value = max(array)
    bucket_count = int(max_value / bucket_size) + 1
    bucket = [[] for _ in range(bucket_count)]
    # 将数组元素分配到各个桶中
    for i in range(length):
        bucket_index = int(array[i] / bucket_size)
        bucket[bucket_index].append(array[i])
    # 对每个桶进行排序
    for i in range(bucket_count):
        bucket[i].sort()
    # 将各个桶中的元素合并到新数组中
    sorted_array_index = 0
    for j in range(bucket_count):
        for k in range(len(bucket[j])):
            array[sorted_array_index] = bucket[j][k]
            sorted_array_index += 1
    return array


if __name__ == '__main__':
    array = [5, 3, 8, 6, 7, 2]
    print(bucket_sort(array))
