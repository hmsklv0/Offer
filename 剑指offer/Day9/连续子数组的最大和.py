class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # 内存开销大
        dp = []
        s = 0

        for i in nums:
            # 状态转移方程
            # 如果之前的 sum 大于0，则继续选择加，否则从当前点重新开始记录
            # 即：1. 要么以当前值为最大值数组的起点
            #    2. 要么从还在之前的数组上继续
            s = max(i, s + i)
            dp.append(s)

        return max(dp)


    def maxSubArray2(self, nums: list[int]) -> int:
        # 时间增多
        max_v = float('-inf')
        s = 0

        for i in nums:
            s = max(i, s + i)
            max_v = max(max_v, s)

        return max_v

