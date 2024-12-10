def fibonacci_search(arr, target):
    # 1. 生成足够长的斐波那契数列
    def generate_fibonacci_until(n):
        fib = [0, 1]
        while fib[-1] < n:
            fib.append(fib[-1] + fib[-2])
        return fib

    # 2. 找到大于等于数组长度的最近的斐波那契数
    n = len(arr)
    fib = generate_fibonacci_until(n)
    k = len(fib) - 1 if fib[-1] >= n else len(fib)

    # 如果数组长度不是斐波那契数，扩展数组
    fib_k = fib[k]
    extended_arr = arr + [arr[-1]] * (fib_k - n)

    # 初始化指针
    low = 0
    high = n - 1

    while low <= high:
        # 3. 计算 mid 值
        mid = low + fib[k - 1] - 1
        # 保证 mid 不越界
        mid = min(mid, high)
        # 进行比较
        if extended_arr[mid] == target:
            # 如果 mid 在原始数组范围内，直接返回
            return mid if mid < n else high
        elif extended_arr[mid] < target:
            # 缩小范围到 [mid+1, high]
            low = mid + 1
            k -= 2
        else:
            # 缩小范围到 [low, mid-1]
            high = mid - 1
            k -= 1
        if k < 2:
            break

    # 没找到目标值
    return -1


# 测试代码
arr = [1, 8, 10, 1000, 10000000, 9999999999]
target = 9999999999
result = fibonacci_search(arr, target)
print("索引为:", result)  # 输出应该是 5
