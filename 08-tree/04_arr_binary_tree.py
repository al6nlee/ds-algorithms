def pre_order(arr: list, index: int):
    if not arr:
        return

    # 向左遍历
    if index * 2 + 1 < len(arr):
        pre_order(arr, index * 2 + 1)

    # 向右遍历
    if index * 2 + 2 < len(arr):
        pre_order(arr, index * 2 + 2)



if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
