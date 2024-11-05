import importlib.util
import sys

# 模块的路径
module_path = './01-stack.py'

# 生成模块名称，这里使用文件名作为模块名称（去除文件扩展名）
module_name = 'module_01_stack'

# 加载模块
spec = importlib.util.spec_from_file_location(module_name, module_path)
module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = module
spec.loader.exec_module(module)

# 现在可以使用模块中的内容，例如类 MyClass
Stack = getattr(module, 'Stack')


class StackPlus(Stack):

    def __init__(self, capacity=10):
        super().__init__(capacity)
        self.priority = {'+': 1, '-': 1, '*': 2, '/': 2}

    def is_operator(self, item):
        return item in self.priority

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


class Calculator(object):
    def __init__(self, expression):
        self.expression = expression
        self.num_stack = StackPlus()
        self.op_stack = StackPlus()
        self.index = 0

    def run(self):
        while self.index < len(self.expression):
            item = self.expression[self.index]
            # 判断是否是运算符
            if self.op_stack.is_operator(item):
                # 判断符号栈是否为空
                if self.op_stack.is_empty():
                    self.op_stack.push(item)
                else:
                    top_op = self.op_stack.peek()
                    # 判断优先级
                    if self.op_stack.priority[top_op] >= self.op_stack.priority[item]:
                        num2 = self.num_stack.pop()
                        num1 = self.num_stack.pop()
                        op = self.op_stack.pop()
                        result = self.num_stack.cal(num1, num2, op)
                        self.num_stack.push(result)
                        self.op_stack.push(item)
                    else:
                        self.op_stack.push(item)
            elif item.isdigit():
                # 处理多位数时，需要向表达式的后面再看一位，定义一个临时变量用于拼接
                num = item
                while self.index + 1 < len(self.expression) and self.expression[self.index + 1].isdigit():
                    self.index += 1
                    num += self.expression[self.index]
                self.num_stack.push(int(num))

            self.index += 1

        while not self.op_stack.is_empty():
            num2 = self.num_stack.pop()
            num1 = self.num_stack.pop()
            op = self.op_stack.pop()
            result = self.num_stack.cal(num1, num2, op)
            self.num_stack.push(result)

        return self.num_stack.pop()


if __name__ == '__main__':
    print(Calculator('7*2*2-5+1-5+3-4').run())
    print(Calculator('3*25-50-4').run())
