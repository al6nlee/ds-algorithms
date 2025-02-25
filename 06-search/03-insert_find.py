def insert_find(lst, item):
    left = 0
    right = len(lst) - 1
    while left <= right and item >= lst[left] and item <= lst[right]:
        print("****")
        mid = left + (right - left) * (item - lst[left]) // (lst[right] - lst[left])  # 使用自适应的插值查找
        if lst[mid] == item:
            return mid
        elif lst[mid] < item:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == '__main__':
    print(insert_find([1, 2, 3, 4, 5, 6, 567, 889, 999], 889))
