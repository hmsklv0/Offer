from typing import List


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
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i-1])
        return dp[nums_len]

a = Solution()
print(a.rob([1,2,3,1]))