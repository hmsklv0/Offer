# https://leetcode.cn/problems/single-number/description/?envType=study-plan-v2&envId=top-100-liked
# 相同数字异或的结果为0

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ret = 0
        for i in nums:
            ret = ret ^ i
        return ret