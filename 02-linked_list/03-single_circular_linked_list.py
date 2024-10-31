class Node:
    def __init__(self, no: int, name: str):
        self.no = no
        self.name = name
        self.next = None

    def __str__(self):
        return f'【Node】 {self.no} {self.name}'


class SingleCircleLinkedList:
    def __init__(self):
        self.first = None
        self.cur = self.first  # 辅助指针

    def add(self, num: int):
        if num < 1:
            return
        for i in range(1, num + 1):
            node = Node(i, f'小孩_{i}')
            if self.first is None:
                self.first = node
            else:
                self.cur.next = node
            self.cur = node
            self.cur.next = self.first

    def list(self):
        if self.first is None:
            print("链表为空")
            return
        cur = self.first
        while cur.next != self.first:
            print(cur)
            cur = cur.next
        print(cur)

    def count(self, start: int, count: int, total: int):
        """
        :param start: 从第几个小孩开始数数
        :param count: 数几下出圈
        :param total: 最开始有多少小孩在圈
        :return:
        """
        if start < 1 or start > total:
            print("输入的参数有误")
            return
        quick = self.first
        slow = self.first
        while slow.next != self.first:  # 将slow指向链表的最后一个元素
            slow = slow.next

        for _ in range(start - 1):  # 快慢指针都移动到start位置
            quick = quick.next
            slow = slow.next

        # 开始报数
        while True:
            if quick == slow:  # 快慢指针相遇，圈中只有一个人，报数完毕
                print(f"最后出圈的小孩是{quick}")
                break
            for _ in range(count - 1):
                quick = quick.next
                slow = slow.next
            print(f"出圈的小孩是{quick}")
            quick = quick.next
            slow.next = quick


if __name__ == '__main__':
    # linked_list = SingleCircleLinkedList()
    # linked_list.add(5)
    # linked_list.list()

    linked_list = SingleCircleLinkedList()
    linked_list.add(5)
    linked_list.count(1, 2, 5)
