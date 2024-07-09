# https://leetcode.cn/problems/FortPu/solutions/1411579/cha-ru-shan-chu-he-sui-ji-fang-wen-du-sh-8pqy/
# 官方题解
import random


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.map = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.map:
            return False
        self.nums.append(val)
        self.map[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.map:
            return False
        # 获取最后一个元素，将该元素替换至val处，数组和map都需要
        index = self.map[val]
        last = self.nums[-1]
        self.nums[index] = last
        self.map[last] = index
        # 删除操作
        self.nums.pop()
        self.map.pop(val)
        return True



    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()