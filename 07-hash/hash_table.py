class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        """根据键获取值"""
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def remove(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False

    def display(self):
        """显示哈希表"""
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")


# 示例用法
if __name__ == "__main__":
    ht = HashTable(size=5)
    ht.insert("apple", 1)
    ht.insert("banana", 2)
    ht.insert("orange", 3)
    ht.display()
    print("Get 'apple':", ht.get("apple"))
    ht.remove("banana")
    ht.display()
