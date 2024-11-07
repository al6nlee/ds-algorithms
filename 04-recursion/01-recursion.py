def t1(n):
    if n > 1:
        t1(n - 1)
    print("n =", n)


def t2(n):
    if n == 1:
        return 1
    return n * t2(n - 1)


if __name__ == '__main__':
    print("打印问题")
    t1(5)
    print("阶乘问题")
    print(t2(5))
