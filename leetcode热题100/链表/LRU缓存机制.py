# 题解 https://leetcode.cn/problems/lru-cache/
# 思路一 借助已有的api快速解题
# 思路二 借助双向链表和哈希表解决
# https://blog.csdn.net/hyyyya/article/details/109300396
# LRU 缓存机制
import collections

class DLinkedNode:
    def __init__(self, key=0, value=0):
        # 前置指针和尾指针保证双向链表
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache(collections.OrderedDict):

    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)

class LRUCache2:
    # 依靠双向链表和哈希表解决
    # 双向链表解决 快速插入和快速删除 的问题
    # 哈希表解决 快速访问的问题
    def __init__(self, capacity: int):
        # 初始化字典
        self.cache_dict = {}
        self.size = 0
        self.capacity = capacity
        # 初始化双向链表
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.pre = self.head


    def get(self, key: int) -> int:
        if key not in self.cache_dict:
            return -1
        else:

            # 节点移到链表最后
            node = self.cache_dict[key]

            # 删除当前节点
            self.move_to_end(node)
            return node.value


    def put(self, key: int, value: int) -> None:
        if key in self.cache_dict:
            node = self.cache_dict[key]
            node.value = value
            self.move_to_end(node)
        else:
            # 添加新节点
            node = DLinkedNode(key, value)
            self.add_to_end(node)
            self.size += 1
            self.cache_dict[key] = node

            if self.size > self.capacity:
                node = self.removeHead()
                self.cache_dict.pop(node.key)
                self.size -= 1

    def move_to_end(self, node: DLinkedNode):
        self.remove_node(node)
        self.add_to_end(node)
        # 移到最后节点, 01 插入
        # node 本身处理

    def add_to_end(self, node: DLinkedNode):
        # 移到最后节点, 01 插入
        # node 本身处理
        node.pre = self.tail.pre
        node.next = self.tail

        # 前置节点和尾节点处理
        self.tail.pre.next = node
        self.tail.pre = node
        
    def remove_node(self, node: DLinkedNode):
        node.pre.next = node.next
        node.next.pre = node.pre

    def removeHead(self):
        node = self.head.next
        self.remove_node(node)

        return node
