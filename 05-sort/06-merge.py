def merge_sort(array):
    """
    归并排序
    :param array: 待排序数组
    :return: 排序后的数组
    """
    if len(array) <= 1:
        return array
    mid = len(array) // 2  # 中间索引
    left, right = array[:mid], array[mid:]
    return meger(merge_sort(left), merge_sort(right))


def meger(left, right):
    """
    合并两个有序数组
    :param left: 左数组
    :param right: 右数组
    :return: 合并后的数组
    """
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


if __name__ == '__main__':
    array = [5, 3, 2, 1, 4]
    print(merge_sort(array))
