"""
使用数组去模拟队列
"""


class ArrayQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.data = [None] * capacity
        self.head = -1
        self.tail = -1

    def is_full(self):
        return self.tail == self.capacity - 1

    def is_empty(self):
        return self.head == self.tail

    def add_que(self, item):
        if self.is_full():
            print("队列已满")
            return
        self.tail += 1
        self.data[self.tail] = item

    def get_que(self):
        if self.is_empty():
            print("队列为空")
            return
        self.head += 1
        return self.data[self.head]

    def show_que(self):
        if self.is_empty():
            print("队列为空")
            return
        return self.data

    def head_que(self):
        if self.is_empty():
            print("队列为空")
            return
        return self.data[self.head + 1]


if __name__ == '__main__':
    q = ArrayQueue(3)
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
