class Queen8(object):
    def __init__(self):
        self.max = 8
        self.queens = [0] * 8
        self.count = 0

    def print_queen(self):
        for row in range(self.max):
            for col in range(self.max):
                if self.queens[row] == col:
                    print("Q  ", end='')
                else:
                    print("*  ", end='')
            print()

    def check(self, n: int) -> bool:
        """
        检查是否可以放置皇后
        :param n: 拜访第n+1个皇后，n=7已经是最大值了
        :return:
        """
        for i in range(n):
            if self.queens[i] == self.queens[n]:  # 判断准备要放置的皇后是否与之前的皇后在同一列
                return False
            elif abs(self.queens[n] - self.queens[i]) == n - i:  # 判断是否在同一斜线
                return False
        return True

    def set_queen(self, n: int):
        """
        放置皇后
        :param n: 摆放第n个皇后
        :return:
        """
        if n == self.max:
            self.count += 1
            self.print_queen()
            print("这是第%d种摆放方法" % self.count)
            return
        for col in range(self.max):
            self.queens[n] = col
            if self.check(n):
                self.set_queen(n + 1)
            else:
                pass  # 一旦 check 不通过，产生冲突，代码就会跳出循环，不需要执行else；这里的for是关键核心


if __name__ == '__main__':
    q8 = Queen8()
    q8.set_queen(0)
