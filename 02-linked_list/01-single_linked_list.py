"""
使用带 head 头的单向链表实现 – 水浒英雄排行榜管理完成对英雄人物的增删改查操作

"""


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

    # 删除
    hero_node1 = HeroNode(1, '宋江', '及时雨')
    hero_node2 = HeroNode(2, '卢俊义', '玉麒麟')
    hero_node3 = HeroNode(3, '吴用', '智多星')
    hero_node4 = HeroNode(4, '林冲', '豹子头')
    hero_list = SingleLinkedList()
    hero_list.add_by_order(hero_node1)
    hero_list.add_by_order(hero_node4)
    hero_list.add_by_order(hero_node2)
    hero_list.add_by_order(hero_node3)
    hero_list.list()
    print("====================删除后====================")
    hero_list.delete(3)
    hero_list.delete(1)
    hero_list.delete(2)
    hero_list.delete(4)
    hero_list.list()
