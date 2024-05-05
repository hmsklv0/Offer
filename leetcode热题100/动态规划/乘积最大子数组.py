# https://leetcode.cn/problems/maximum-product-subarray/solutions/250015/cheng-ji-zui-da-zi-shu-zu-by-leetcode-solution/?envType=study-plan-v2&envId=top-100-liked
# 增加一个辅助的最小状态转移

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        nums_len = len(nums)
        dp = [0 for _ in range(nums_len+1)]
        dp_min = [0 for _ in range(nums_len+1)]
        dp[0] = 1
        dp_min[0] = 1

        result = float('-inf')
        for i in range(1, nums_len +1):
            if nums[i-1] != 0:
                dp[i] = max(dp[i-1]* nums[i-1],dp_min[i-1]*nums[i-1], nums[i-1])
                dp_min[i] = min(dp[i-1]*nums[i-1], dp_min[i-1]*nums[i-1], nums[i-1])
            result = max(result, dp[i], dp_min[i])
        return result


    def maxProduct2(self, nums: List[int]) -> int:
        # 1 dp 记录当前以 nums[i] 结尾的子数组的最大值
        # 1 dp_min 记录当前以 nums[i] 结尾的子数组的最小值
        dp = [1 for i in range(len(nums))]
        dp_min = [1 for i in range(len(nums))]

        # 2 递推公式，状态转移方程
        # dp[i] = max(nums[i], dp[i-1] * nums[i], dp_min[i-1] * nums[i])
        # dp_min[i] = min(nums[i], dp[i-1] * nums[i], dp_min[i-1] * nums[i])

        # 3 初始化
        dp[0] = nums[0]
        dp_min[0] = nums[0]

        # 4 遍历方式
        res = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] * nums[i], dp_min[i - 1] * nums[i])
            dp_min[i] = min(nums[i], dp[i - 1] * nums[i], dp_min[i - 1] * nums[i])
            res = max(res, dp[i])
        return res

