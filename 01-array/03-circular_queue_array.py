"""
使用数组去模拟环形队列
"""


class ArrayQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.data = [None] * capacity
        self.head = 0
        self.tail = 0

    def is_full(self):
        return (self.tail + 1) % self.capacity == self.head

    def is_empty(self):
        return self.head == self.tail

    def add_que(self, item):
        if self.is_full():
            print(f"队列已满, head:{self.head}, tail: {self.tail}")
            return
        self.data[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity

    def get_que(self):
        if self.is_empty():
            print("队列为空")
            return
        value = self.data[self.head]
        self.head = (self.head + 1) % self.capacity
        return value

    def show_que(self):
        if self.is_empty():
            print("队列为空")
            return
        # 从head开始遍历，遍历 valid_num 个有效数据
        valid_num = (self.tail + self.capacity - self.head) % self.capacity
        current_list = []
        for i in range(valid_num):
            current_list.append(self.data[(self.head + i) % self.capacity])
        return current_list

    def head_que(self):
        if self.is_empty():
            print("队列为空")
            return
        return self.data[self.head]


if __name__ == '__main__':
    q = ArrayQueue(4)  # 实际存放的有效数据，只有3个，因为head到tail之间，最后tail是预留的空位
    while True:
        print("================系统================")
        print("a: add添加数据")
        print("g: get取出数据")
        print("s: show队列所有查看数据")
        print("h: head查看头数据")
        print("q: quit退出")
        print("====================================")
        option = input("请输入你的选择：")
        if option == "a":
            item = input("请输入要添加的数据：")
            q.add_que(item)
        elif option == "g":
            print(q.get_que())
        elif option == "s":
            print(q.show_que())
        elif option == "h":
            print(q.head_que())
        elif option == "q":
            break
