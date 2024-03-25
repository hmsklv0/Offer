# https://www.programmercarl.com/0416.%E5%88%86%E5%89%B2%E7%AD%89%E5%92%8C%E5%AD%90%E9%9B%86.html#%E6%80%9D%E8%B7%AF
# 01 背包问题

from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        all = sum(nums)
        if all % 2 == 1:
            return False
        target = all // 2
        dp = [0 for _ in range(target + 1)]

        for i in range(len(nums)):
            for j in range(target, nums[i]-1, -1):
                dp[j] = max(dp[j], dp[j-nums[i]]+ nums[i])
        if dp[target] == target:
            return True
        else:
            return False