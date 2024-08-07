# https://programmercarl.com/0674.%E6%9C%80%E9%95%BF%E8%BF%9E%E7%BB%AD%E9%80%92%E5%A2%9E%E5%BA%8F%E5%88%97.html
# https://leetcode.cn/problems/longest-increasing-subsequence/solutions/2279668/dai-ma-sui-xiang-lu-leetcode300zui-chang-sh5m/?envType=study-plan-v2&envId=top-100-liked

#
# https://www.programmercarl.com/0300.%E6%9C%80%E9%95%BF%E4%B8%8A%E5%8D%87%E5%AD%90%E5%BA%8F%E5%88%97.html#%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E7%89%88%E6%9C%AC
# 题解
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        nums_len = len(nums)
        dp = [1 for _ in range(nums_len + 1)]
        dp[0] = 0
        if nums_len == 1:
            return 1

        result = 0
        for i in range(2, nums_len + 1):
            for j in range(1, i):
                if nums[i - 1] > nums[j - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)
            # 不用在dp[i]中 保留之前的最长递增子序列，每个dp[i]只保留自己对应的最长递增子序列
            result = max(result, dp[i])
        print(dp)
        return result

    def lengthOfLIS2(self, nums: List[int]) -> int:

        # 1 dp[i] 代表以 nums[i] 结尾的 最长递增子序列 的长度
        dp = [1 for i in range(len(nums))]

        # 2 递推公式，状态转移方程
        # 对 nums[i] 遍历从 0 到 i-1 中所有的子序列
        # 取子序列的最大值
        # if nums[i] > nums[j]:
        #     dp[i] = max(dp[i], dp[j] + 1)

        # 3 初始化
        # nums = [1]
        # 以 1 结尾的数组怎么找子序列的长度？
        # 因此初始化就应该为1
        # dp[0] = 1

        # 4 遍历顺序
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            # print(dp)

        return max(dp)
