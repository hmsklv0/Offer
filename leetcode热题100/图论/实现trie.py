# https://leetcode.cn/problems/implement-trie-prefix-tree/solutions/717239/shi-xian-trie-qian-zhui-shu-by-leetcode-ti500/?envType=study-plan-v2&envId=top-100-liked
# 思路：将字典树设计为26叉树
# 每个节点的子树有26个，对应26个字母
# 同时每个节点设置为布尔类型，判断当前字段是否属于某个字符串的结尾

class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def insert(self, word: str) -> None:
        # 根据字符进行判断，遍历子树插入
        node = self
        for i in word:
            index = ord(i) - ord('a')
            if node.children[index] is None:
                node.children[index] = Trie()
            node = node.children[index]
        node.isEnd = True

    def search(self, word: str) -> bool:
        # 结尾判断是否为True
        node = self
        for i in word:
            index = ord(i) - ord('a')
            if node.children[index] is None:
                return False
            node = node.children[index]
        if node is None or node.isEnd is False:
            return False
        else:
            return True

    def startsWith(self, prefix: str) -> bool:
        # 只需要判断前缀就可以了
        node = self
        for i in prefix:
            index = ord(i) - ord('a')
            if node.children[index] is None:
                return False
            node = node.children[index]
        if node is None:
            return False
        else:
            return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
