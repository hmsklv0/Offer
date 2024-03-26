# https://programmercarl.com/0209.%E9%95%BF%E5%BA%A6%E6%9C%80%E5%B0%8F%E7%9A%84%E5%AD%90%E6%95%B0%E7%BB%84.html#%E6%80%9D%E8%B7%AF
# 思路：滑动窗口
# 思路2：前缀和 + 二分查找
# n + nlog(n)
# 遍历得到前缀和后，每次将当前的前缀和 + target，然后到前缀和数组中去找对应的位置

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        cur_sum = 0
        res = float('inf')
        while right < len(nums):
            cur_sum += nums[right]
            # 动态变化的滑动窗口，右边界不断向右扩张
            # 一旦大于目标值，左边界收缩
            if cur_sum >= target:
                res = min(res, right - left + 1)
                cur_sum -= nums[left]
                left += 1
        return res if res < float('inf') else 0
