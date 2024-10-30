"""
思路分析-五子棋盘
二维数组 -> 稀疏数组
1. 遍历原始二维数组，得到所有有效值
2. 根据有效数据，创建稀疏数据组
3. 将所有的有效数据存放到稀疏数组上

稀疏数组 -> 二维数组
1. 读取稀疏数组的第一行，根据第一行创建二维数组
2. 再读取稀疏数组后面有效数据，赋值给二维数组
"""


def to_sparse_array(array):
    """
    将二维数组转换为稀疏数组
    :param array: 二维数组
    :return: 稀疏数组
    """
    # 1. 遍历原始二维数组，得到所有有效值
    row_count = len(array)
    col_count = len(array[0])
    valid_count = 0
    for row in range(row_count):
        for col in range(col_count):
            if array[row][col] != 0:
                valid_count += 1

    sparse_array = [[row_count, col_count, valid_count]]
    for row in range(row_count):
        for col in range(col_count):
            if array[row][col] != 0:
                sparse_array.append([row, col, array[row][col]])
    print("打印:生成后的稀疏数组")
    for item in sparse_array:
        for i in item:
            print(i, end=' ')
        print('\t')
    return sparse_array


def to_array(sparse_array):
    """
    将稀疏数组转换为二维数组
    :param sparse_array: 稀疏数组
    :return: 二维数组
    """
    row_count, col_count, valid_count = sparse_array[0]
    array = [[0 for _ in range(col_count)] for _ in range(row_count)]
    for row in range(1, valid_count + 1):
        array[sparse_array[row][0]][sparse_array[row][1]] = sparse_array[row][2]
    print("打印:生成后的二维数组")
    for row in array:
        for item in row:
            print(item, end=' ')
        print('\t')
    return array


if __name__ == '__main__':
    array = [[0, 0, 0], [1, 1, 2], [0, 0, 1], [0, 2, 0]]
    sparse_array = to_sparse_array(array)
    array = to_array(sparse_array)
