from typing import List
# https://leetcode.cn/problems/house-robber/solutions/138131/dong-tai-gui-hua-jie-ti-si-bu-zou-xiang-jie-cjavap/?envType=study-plan-v2&envId=top-100-liked
# https://programmercarl.com/0198.%E6%89%93%E5%AE%B6%E5%8A%AB%E8%88%8D.html
# 代码随想录题解

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        nums_len = len(nums)
        dp = [0 for _ in range(nums_len + 1)]
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, nums_len + 1):
            # 比较前一个数 dp[i - 1],
            # 与 前两个数 dp[i - 2] + nums[i]
            # 更大者为最优选择
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        return dp[nums_len]

    def rob2(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        nums_len = len(nums)
        # dpi 指 偷到第 i + 1 家时，能偷取的最大金额
        dp = [0 for _ in range(nums_len)]

        # 确定递推公式
        # dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        # 初始化
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, nums_len):
            # 比较前一个数 dp[i - 1],
            # 与 前两个数 dp[i - 2] + nums[i]
            # 更大者为最优选择
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]

    def rob3(self, nums: List[int]) -> int:
        # 优化内存写法
        if len(nums) <= 2:
            return max(nums)
        nums_len = len(nums)

        # dpi 指 偷到第 i + 1 家时，能偷取的最大金额
        dpi = 0

        # 确定递推公式
        # dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        # 初始化
        dp0 = nums[0]
        dp1 = max(nums[0], nums[1])

        for i in range(2, nums_len):
            # 比较前一个数 dp[i - 1],
            # 与 前两个数 dp[i - 2] + nums[i]
            # 更大者为最优选择
            dpi = max(dp1, dp0 + nums[i])
            dp0 = dp1
            dp1 = dpi
        return dpi
a = Solution()
print(a.rob([1, 2, 3, 1]))
