"""
使用带 head 头的单向链表实现 – 水浒英雄排行榜管理完成对英雄人物的增删改查操作

"""
from collections import deque


class HeroNode:
    def __init__(self, no: int, name: str, nickname: str):
        self.no = no
        self.name = name
        self.nickname = nickname
        self.next = None

    def __str__(self):
        return "HeroNode 【no: %d, name: %s, nickname: %s】" % (self.no, self.name, self.nickname)


class SingleLinkedList:
    def __init__(self):
        self.head = HeroNode(0, '', '')

    def add(self, hero_node: HeroNode):
        temp: HeroNode = self.head
        while temp.next:
            temp = temp.next
        temp.next = hero_node

    def add_by_order(self, hero_node: HeroNode):
        """
        1. 先通过辅助节点，根据下一个节点的no进行定位
        2. 如果找到了，则将 hero_node 的 next 指向下一个节点，辅助节点的 next 指向 hero_node
        :param hero_node:
        :return:
        """
        temp: HeroNode = self.head
        while temp.next:
            if temp.next.no > hero_node.no:
                hero_node.next = temp.next
                break
            elif temp.next.no == hero_node.no:
                print("添加英雄编号 %d 已经存在，不能添加" % hero_node.no)
                return
            else:
                temp = temp.next
        temp.next = hero_node

    def list(self):
        temp: HeroNode = self.head
        if not temp.next:
            print("链表为空")
            return
        while temp.next:
            temp = temp.next
            print(temp)

    def update(self, hero_node: HeroNode):
        temp: HeroNode = self.head
        while temp.next:
            if temp.next.no == hero_node.no:  # 遍历到倒数第二个节点都没有找到待删除的节点，则可以认为没有找到
                temp.next.name = hero_node.name
                temp.next.nickname = hero_node.nickname
                return
            temp = temp.next
        print("没有找到编号为 %d 的英雄" % hero_node.no)

    def delete(self, no: int):
        temp: HeroNode = self.head
        while temp.next:
            if temp.next.no == no:
                temp.next = temp.next.next
                return
            temp = temp.next
        print("没有找到编号为 %d 的英雄" % no)

    def length(self):
        temp: HeroNode = self.head
        count = 0
        while temp.next:
            count += 1
            temp = temp.next
        return count

    def find_last_k_node(self, k: int):
        # 先把链表从头到尾遍历，获取链表的长度
        # 获取到链表的长度后，从头遍历到 (length - k) 个节点，就是倒数第k个节点
        temp: HeroNode = self.head
        if k <= 0 or k > self.length():
            print(f"参数有误,当前链表长度为{self.length()}")
            return None
        for i in range(self.length() + 1 - k):
            temp = temp.next
        return temp

    def reverse_list_by_stack(self):
        """
        利用栈，倒序输出
        :return:
        """
        temp: HeroNode = self.head
        stack = deque()
        while temp.next:
            stack.append(temp.next)
            temp = temp.next
        while len(stack) > 0:
            print(stack.pop())

    def reverse_list(self):
        """
        头插法，双指针
        1. 定义一个临时头节点reverseHead，初始化为一个新的head
        2. 从头到尾遍历原来的链表，没遍历一个节点，将其取出，并插入到链表的最前端
        3. 原来的链表的头节点的next指向临时头节点reverseHead的next
        :return:
        """
        temp: HeroNode = self.head
        reverse_head: HeroNode = HeroNode(0, '', '')
        while temp.next:
            next_node: HeroNode = temp.next  # 双指针，临时变量保存当前节点
            temp.next = next_node.next
            next_node.next = reverse_head.next  # 插入到新的链表
            reverse_head.next = next_node  # 插入到新的链表
        self.head.next = reverse_head.next


if __name__ == '__main__':
    # # 新节点直接追加到尾部
    # hero_node1 = HeroNode(1, '宋江', '及时雨')
    # hero_node2 = HeroNode(2, '卢俊义', '玉麒麟')
    # hero_node3 = HeroNode(3, '吴用', '智多星')
    # hero_node4 = HeroNode(4, '林冲', '豹子头')
    # hero_list = SingleLinkedList()
    # hero_list.add(hero_node1)
    # hero_list.add(hero_node2)
    # hero_list.add(hero_node3)
    # hero_list.add(hero_node4)
    # hero_list.list()

    # # 新节点根据 no的顺序 插入
    # hero_node1 = HeroNode(1, '宋江', '及时雨')
    # hero_node2 = HeroNode(2, '卢俊义', '玉麒麟')
    # hero_node3 = HeroNode(2, '吴用', '智多星')
    # hero_node4 = HeroNode(4, '林冲', '豹子头')
    # hero_list = SingleLinkedList()
    # hero_list.add_by_order(hero_node1)
    # hero_list.add_by_order(hero_node4)
    # hero_list.add_by_order(hero_node2)
    # hero_list.add_by_order(hero_node3)
    # hero_list.list()

    # # 修改
    # hero_node1 = HeroNode(1, '宋江', '及时雨')
    # hero_node2 = HeroNode(2, '卢俊义', '玉麒麟')
    # hero_node3 = HeroNode(3, '吴用', '智多星')
    # hero_node4 = HeroNode(4, '林冲', '豹子头')
    # hero_list = SingleLinkedList()
    # hero_list.add_by_order(hero_node1)
    # hero_list.add_by_order(hero_node4)
    # hero_list.add_by_order(hero_node2)
    # hero_list.add_by_order(hero_node3)
    # hero_list.list()
    # print("====================修改后====================")
    # hero_list.update(HeroNode(3, '吴用1', '智多星1'))
    # hero_list.list()
    # print("====================修改后(未找到)====================")
    # hero_list.update(HeroNode(6, '吴用1', '智多星1'))
    # hero_list.list()

    # # 删除
    # hero_node1 = HeroNode(1, '宋江', '及时雨')
    # hero_node2 = HeroNode(2, '卢俊义', '玉麒麟')
    # hero_node3 = HeroNode(3, '吴用', '智多星')
    # hero_node4 = HeroNode(4, '林冲', '豹子头')
    # hero_list = SingleLinkedList()
    # hero_list.add_by_order(hero_node1)
    # hero_list.add_by_order(hero_node4)
    # hero_list.add_by_order(hero_node2)
    # hero_list.add_by_order(hero_node3)
    # hero_list.list()
    # print("====================删除后====================")
    # hero_list.delete(3)
    # hero_list.delete(1)
    # hero_list.delete(2)
    # hero_list.delete(4)
    # hero_list.list()

    # # 面试题，统计单向链表，统计有效节点数
    # hero_node1 = HeroNode(1, '宋江', '及时雨')
    # hero_node2 = HeroNode(2, '卢俊义', '玉麒麟')
    # hero_node3 = HeroNode(3, '吴用', '智多星')
    # hero_node4 = HeroNode(4, '林冲', '豹子头')
    # hero_list = SingleLinkedList()
    # hero_list.add_by_order(hero_node1)
    # hero_list.add_by_order(hero_node4)
    # hero_list.add_by_order(hero_node2)
    # hero_list.add_by_order(hero_node3)
    # hero_list.list()
    # print(hero_list.length())
    #
    # # 查找单项列表，倒数第k个节点
    # print(hero_list.find_last_k_node(4))

    # # 反转单链表
    # hero_node1 = HeroNode(1, '宋江', '及时雨')
    # hero_node2 = HeroNode(2, '卢俊义', '玉麒麟')
    # hero_node3 = HeroNode(3, '吴用', '智多星')
    # hero_list = SingleLinkedList()
    # hero_list.add_by_order(hero_node1)
    # hero_list.add_by_order(hero_node2)
    # hero_list.add_by_order(hero_node3)
    # hero_list.list()
    # print()
    # hero_list.reverse_list()
    # hero_list.list()

    # 利用栈，倒序输出
    hero_node1 = HeroNode(1, '宋江', '及时雨')
    hero_node2 = HeroNode(2, '卢俊义', '玉麒麟')
    hero_node3 = HeroNode(3, '吴用', '智多星')
    hero_list = SingleLinkedList()
    hero_list.add_by_order(hero_node1)
    hero_list.add_by_order(hero_node2)
    hero_list.add_by_order(hero_node3)
    hero_list.reverse_list_by_stack()
