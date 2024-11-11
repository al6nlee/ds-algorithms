import random
import time


def shell_sort1(array):
    """
    希尔排序，交换法（效率比较低）
    :param array: 待排序数组
    :return: 排序后的数组
    """
    length = len(array)
    gap = length // 2  # 初始化步长
    while gap > 0:
        for i in range(gap, length):
            j = i
            while j >= gap and array[j - gap] > array[j]:
                array[j], array[j - gap] = array[j - gap], array[j]  # 交换元素
                j -= gap
        gap //= 2
    return array


def shell_sort2(array):
    """
    希尔排序，移位法
    :param array: 待排序数组
    :return: 排序后的数组
    """
    length = len(array)
    gap = length // 2  # 初始化步长
    while gap > 0:
        for i in range(gap, length):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]  # 移位法，逐个将数据后移，最终在合适的位置插入temp
                j -= gap
            array[j] = temp
        gap //= 2
    return array


if __name__ == '__main__':
    data = [random.randint(1, 100000) for _ in range(800000)]

    data_copy1 = data.copy()  # 拷贝数据，避免影响其他测试
    start_time = time.time()
    shell_sort1(data_copy1)
    end_time = time.time()
    print(f"交换法耗时: {end_time - start_time:.2f} 秒")  # 6.15

    data_copy2 = data.copy()  # 拷贝数据，避免影响其他测试
    start_time = time.time()
    shell_sort2(data_copy2)
    end_time = time.time()
    print(f"移位法耗时: {end_time - start_time:.2f} 秒")  # 4.78
