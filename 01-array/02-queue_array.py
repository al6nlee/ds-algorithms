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
    q.add_que(1)
    q.add_que(2)
    q.add_que(3)
    q.add_que(4)  # 队列已满
    print(q.get_que())
    # print(q.get_que())
    # print(q.get_que())

    print(q.show_que())
    print(q.head_que())
