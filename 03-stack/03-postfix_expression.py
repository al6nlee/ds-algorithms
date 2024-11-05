"""
逆波兰计算器
"""
from collections import deque

stack = deque()


class Calculator(object):
    def __init__(self, expression: str):
        self.expression = expression.split(" ")

    def cal(self, num1, num2, op):
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        elif op == '/':
            return num1 / num2
        return 0

    def run(self):
        for item in self.expression:
            if item.isdigit():
                stack.append(item)
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(self.cal(int(num1), int(num2), item))
                # stack.append(eval(f"{num1}{item}{num2}"))
        return stack.pop()


if __name__ == '__main__':
    calculator = Calculator("3 37 + 5 * 6 -")
    print(calculator.run())
