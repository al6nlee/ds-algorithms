class HeroNode:
    def __init__(self, no: int, name: str):
        self.no = no
        self.name = name
        self.left = None
        self.right = None

    def __str__(self):
        return f"HeroNode(no={self.no}, name='{self.name}')"

    def pre_oder_search(self, target):
        """
        1. 先判断当前节点是否是要查找的节点
        2. 如果是，则直接返回
        3. 如果不是，则判断左子节点是否为空，如果不为空，则继续递归查找，如果为空，跳出本次递归
        4. 之后再判断右子节点。。。
        :param target:
        :return:
        """
        global m
        m += 1
        if self.no == target:
            return self
        if self.left:
            result = self.left.pre_oder_search(target)
            if result:
                return result
        if self.right:
            result = self.right.pre_oder_search(target)
            if result:
                return result
        # 如果都没有找到
        return None

    def in_oder_search(self, target):
        """
        1. 判断当前节点左子节点是否为空，如果不为空，则向左递归查找
        2. 如果找打，则返回；否则继续
        3. 向右递归
        :param target:
        :return:
        """
        if self.left:
            result = self.left.in_oder_search(target)
            if result:
                return result
        global m
        m += 1
        if self.no == target:
            return self

        if self.right:
            result = self.right.in_oder_search(target)
            if result:
                return result

    def post_oder_search(self, target):
        """
        1. 首先向左判断
        2. 然后向右判断
        3. 最后判断自身
        """
        if self.left:
            result = self.left.post_oder_search(target)
            if result:
                return result

        if self.right:
            result = self.right.post_oder_search(target)
            if result:
                return result
        global m
        m += 1
        if self.no == target:
            return self


class BinaryTree:
    def __init__(self, root: HeroNode):
        self.root = root

    def pre_oder_search(self, target):
        return self.root.pre_oder_search(target)

    def in_oder_search(self, target):
        return self.root.in_oder_search(target)

    def post_oder_search(self, target):
        return self.root.post_oder_search(target)


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
    m = 0
    print("前序查找：")
    print(binary_tree.pre_oder_search(5))
    print(f"遍历次数: {m}")
    m = 0
    print("中序查找：")
    print(binary_tree.in_oder_search(5))
    print(f"遍历次数: {m}")
    m = 0
    print("后序查找：")
    print(binary_tree.post_oder_search(5))
    print(f"遍历次数: {m}")
