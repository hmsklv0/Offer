# https://mp.weixin.qq.com/s/zXNgpOoFc8K6Lx3FqUkXMg
# 一个简单的思想，如果前缀+当前值 小于 当前值本身，那么重新开始记录子数组和
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        res = nums[0]
        # 借助动态规划的思想，逐个添加，在这个过程中记录连续子数组和
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i - 1] + nums[i])
            res = max(res, nums[i])
        return res

    def maxSubArray2(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        res = nums[0]
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        # 借助动态规划的思想，逐个添加，在这个过程中记录连续子数组和
        # dp 记录以 i 结尾的最大连续子数组和
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            res = max(res, dp[i])
        return res


a = Solution()
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums = [-2, -1]
print(a.maxSubArray(nums))
