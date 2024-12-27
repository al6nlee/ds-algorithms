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

    def delete_node(self, no):
        if self.right and self.right.no == 3:
            a = 1
        if self.left is not None and self.left.no == no:
            self.left = None
            return True
        if self.right is not None and self.right.no == no:
            self.right = None
            return True

        if self.left is not None:
            if self.left.delete_node(no):
                return True
        if self.right is not None:
            if self.right.delete_node(no):
                return True


class BinaryTree:
    def __init__(self, root: HeroNode):
        self.root = root

    def pre_order(self):
        if self.root is None:
            return
        self.root.pre_order()

    def delete_node(self, no):
        if self.root is not None:
            if self.root.no == no:
                self.root = None
                return True
            return self.root.delete_node(no)


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

    binary_tree.delete_node(3)
    binary_tree.pre_order()  # 原来 1 -> 2 -> 3 -> 5 -> 4   ==>  1 -> 2
