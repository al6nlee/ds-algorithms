class Stack:
    def __init__(self, capacity=10):
        self.items = []  # 使用数组模拟栈
        self.capacity = capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, item):
        if self.is_full():
            raise Exception("Stack Overflow")
        self.items.append(item)
        self.top += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack empty")
        self.top -= 1
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack empty")
        return self.items[self.top]

    def list_all(self):
        """
        遍历时，需要从栈顶开始显示数据
        :return:
        """
        if self.is_empty():
            raise Exception("Stack empty")

        for i in range(self.top, -1, -1):
            print(self.items[i])


if __name__ == '__main__':
    # stack = Stack()
    # stack.push(1)
    # stack.push(2)
    # stack.push(3)
    # print(stack.pop())
    # print(stack.pop())
    # print(stack.pop())
    # # print(stack.pop())   # Exception: Stack empty
    # print(stack.is_full())

    stack = Stack(5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.list_all()
