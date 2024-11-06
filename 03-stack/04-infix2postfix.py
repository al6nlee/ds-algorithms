"""
中缀表达式转后缀表达式
"""

from collections import deque


class Infix2Postfix:
    def __init__(self, expression: str):
        self.expression = expression
        self.index = 0  # 用于遍历表达式
        self.s1 = deque()  # 用于存放临时运算符
        self.s2 = []  # 用于存放中间结果的栈，由于最后结果还需要倒序，所以使用队列即可
        self.priority = {'+': 1, '-': 1, '*': 2, '/': 2}

    def to_postfix(self):
        for item in self.expression:
            if item.isdigit():
                num = item
                while self.index + 1 < len(self.expression) and self.expression[self.index + 1].isdigit():
                    self.index += 1
                    num += self.expression[self.index]
                self.s2.append(int(num))
            elif item == '(':
                self.s1.append(item)
            elif item == ')':
                while self.s1[-1] != '(':
                    self.s2.append(self.s1.pop())
                self.s1.pop()
            elif item in ['+', '-', '*', '/']:
                while self.s1 and self.s1[-1] != '(' and self.priority[item] <= self.priority[self.s1[-1]]:
                    self.s2.append(self.s1.pop())
                else:
                    self.s1.append(item)
            self.index += 1
        while self.s1:
            self.s2.append(self.s1.pop())
        return self.s2


if __name__ == '__main__':
    expression = '1+((2+3)*4)-5'
    print(Infix2Postfix(expression).to_postfix())  # [1, 2, 3, '+', 4, '*', '+', 5, '-']
