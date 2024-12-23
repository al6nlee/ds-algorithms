class HeroNode:
    def __init__(self, no: int, name: str):
        self.no = no
        self.name = name
        self.left = None
        self.right = None

    def __str__(self):
        return f"HeroNode(no={self.no}, name='{self.name}')"

    # 前序遍历
    def pre_order(self):
        print(self)
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    # 中序遍历
    def in_order(self):
        """
        1. 先判断左子节点是否为空，不为空，继续中序遍历
        2. 如果为空，则输出该节点
        3. 输出父节点
        4. 再判断右子节点是否为空，不为空，则继续递归中序遍历
        :return:
        """
        if self.left:
            self.left.in_order()
            print(self)  # 输出当前节点，也就是父节点z
            if self.right:
                self.right.in_order()
                return
        print(self)
        if self.right:
            self.right.in_order()


    # 后序遍历
    def post_order(self):
        """
        1. 先判断左子节点是否为空，不为空，则继续后序遍历
        2. 如果为空，则输出当前节点
        3. 紧接着判断右子节点是否为空，不为空则继续后序遍历
        4. 在右子节点输出后再输出父节点
        :return:
        """
        if self.left:
            self.left.post_order()
            if self.right:
                self.right.post_order()
                print(self)
                return
            return
        if self.right:
            self.right.post_order()
        print(self)


class BinaryTree:
    def __init__(self, root: HeroNode):
        self.root = root

    def pre_order(self):
        if self.root is None:
            return
        self.root.pre_order()

    def in_order(self):
        if self.root is None:
            return
        self.root.in_order()

    def post_order(self):
        if self.root is None:
            return
        self.root.post_order()


if __name__ == '__main__':
    hero_1 = HeroNode(1, '宋江')
    hero_2 = HeroNode(2, '吴用')
    hero_3 = HeroNode(3, '卢俊义')
    hero_4 = HeroNode(4, '林冲')
    hero_5 = HeroNode(5, '宗盛')

    # 手动创建二叉数，后面递归创建二叉树
    binary_tree = BinaryTree(hero_1)
    binary_tree.root.left = hero_2
    binary_tree.root.right = hero_3
    binary_tree.root.right.left = hero_5
    binary_tree.root.right.right = hero_4

    binary_tree.pre_order()  # 1 -> 2 -> 3 -> 5 -> 4
    print()
    binary_tree.in_order()  # 2 -> 1 -> 5 -> 3 -> 4
    print()
    binary_tree.post_order()  # 2 -> 5 -> 4 -> 3 -> 1
