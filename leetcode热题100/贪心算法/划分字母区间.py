# https://programmercarl.com/0763.%E5%88%92%E5%88%86%E5%AD%97%E6%AF%8D%E5%8C%BA%E9%97%B4.html#%E6%80%9D%E8%B7%AF

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash_table = [0 for _ in range(26)]
        # 得到每个字母的最远距离
        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            hash_table[index] = i

        # 利用最远距离进行拼接
        result = []
        left, right = 0, 0
        for i in range(len(s)):
            s_index = ord(s[i]) - ord('a')
            right = max(right, hash_table[s_index])
            # 字段拼接，到此为止,
            # 注意结束条件：字符遍历到当前的所能划分片段中所有字符的最远距离
            if right == i:
                result.append(right - left + 1)
                left = i + 1
        return result
