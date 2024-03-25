# https://programmercarl.com/0045.%E8%B7%B3%E8%B7%83%E6%B8%B8%E6%88%8FII.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# 题解
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # 动态规划
        n = len(nums)
        # dp[i]代表走到第i个位置需要的最少步数
        dp = [float('inf') for i in range(n)]

        dp[0] = 0
        # 递推公式
        # dp[i+j] = min(dp[i+j], dp[i] + 1)
        for i in range(n):
            for j in range(1, nums[i] + 1):
                if i + j <= n - 1:
                    dp[i + j] = min(dp[i + j], dp[i] + 1)
        print(dp)
        return dp[n - 1]

    def jump2(self, nums: List[int]) -> int:
        # 贪心算法
        # 核心思想 分为两层覆盖区域
        # 第一层 本次覆盖区域，如果遍历到末尾
        # 第二层 下一次最长覆盖区域，如果大于长度，那么进入下一层
        # 由第一层跳向第二层，记为 跳跃一次
        n = len(nums)

        cover = 0
        next_cover = 0
        step = 0

        for i in range(n):
            next_cover = max(next_cover, i + nums[i])
            if i == cover:
                print(cover, next_cover)
                if cover >= n - 1:
                    break
                step += 1
                cover = next_cover


        return step


a = Solution()
nums = [2, 3, 1, 1, 4]
# nums = [0]
print(a.jump2(nums))
