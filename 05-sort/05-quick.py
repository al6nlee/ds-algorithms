def quick_sort(array):
    """
    快速排序
    :param array: 待排序数组
    :return: 排序后的数组
    """
    if len(array) <= 1:
        return array
    pivot = array[0]  # 选择一个基准值，这里选第一个
    left = [i for i in array[1:] if i <= pivot]
    right = [i for i in array[1:] if i > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == '__main__':
    array = [5, 2, 3, 2, 1]
    sorted_array = quick_sort(array)
    print(sorted_array)
