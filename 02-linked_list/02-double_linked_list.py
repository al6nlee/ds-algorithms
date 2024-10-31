class DoubleNode:
    def __init__(self, no: int, name: str, nickname: str):
        self.no = no
        self.name = name
        self.nickname = nickname
        self.pre = None
        self.next = None

    def __str__(self):
        return "HeroNode[{},{},{}]".format(self.no, self.name, self.nickname)


class DoubleLinkedList:
    def __init__(self):
        self.head = DoubleNode(0, '', '')

    def add(self, hero_node: DoubleNode):
        node = self.head
        while node.next:
            node = node.next
        node.next = hero_node
        hero_node.pre = node

    def add_by_order(self, hero_node: DoubleNode):
        node = self.head
        while node.next:
            if node.next.no > hero_node.no:
                hero_node.next = node.next
                hero_node.pre = node
                node.next.pre = hero_node
                node.next = hero_node
                return
            elif node.next.no == hero_node.no:
                print("添加英雄编号 %d 已经存在，不能添加" % hero_node.no)
                return
            else:
                node = node.next
        node.next = hero_node
        hero_node.pre = node

    def list(self):
        node = self.head
        if not node.next:
            print("链表为空")
            return
        while node.next:
            node = node.next
            print(node)

    def update(self, hero_node: DoubleNode):
        node = self.head
        while node.next:
            if node.next.no == hero_node.no:
                node.next.name = hero_node.name
                node.next.nickname = hero_node.nickname
                return
            node = node.next
        print("没有找到编号为 %d 的英雄" % hero_node.no)

    def delete(self, no: int):
        node = self.head
        while node.next:
            if node.next.no == no:
                node.next = node.next.next
                if node.next:
                    node.next.pre = node
                return
            node = node.next


if __name__ == '__main__':
    # hero_1 = DoubleNode(1, '宋江', '及时雨')
    # hero_2 = DoubleNode(2, '卢俊义', '玉麒麟')
    # hero_3 = DoubleNode(3, '吴用', '智多星')
    # hero_4 = DoubleNode(4, '林冲', '豹子头')
    # hero_5 = DoubleNode(4, '林冲1', '豹子头1')
    # hero_list = DoubleLinkedList()
    # hero_list.add(hero_1)
    # hero_list.add(hero_2)
    # hero_list.add(hero_3)
    # hero_list.add(hero_4)
    # hero_list.list()
    # print("update")
    # hero_list.update(hero_5)
    # hero_list.list()
    # print("delete")
    # hero_list.delete(4)
    # hero_list.list()

    hero_1 = DoubleNode(1, '宋江', '及时雨')
    hero_2 = DoubleNode(2, '卢俊义', '玉麒麟')
    hero_3 = DoubleNode(3, '吴用', '智多星')
    hero_4 = DoubleNode(4, '林冲', '豹子头')
    hero_list = DoubleLinkedList()
    hero_list.add_by_order(hero_1)
    hero_list.add_by_order(hero_3)
    hero_list.add_by_order(hero_2)
    hero_list.add_by_order(hero_4)
    hero_list.list()
