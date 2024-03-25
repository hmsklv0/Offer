# 二分查找题解 https://mp.weixin.qq.com/s/jBEmRfBUHq-NNvXWbRpHKQ
# 快慢指针题解 https://leetcode.cn/problems/find-the-duplicate-number/solutions/58841/287xun-zhao-zhong-fu-shu-by-kirsche/?envType=study-plan-v2&envId=top-100-liked
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 二分查找的思想
        nums_len = len(nums)
        n = nums_len - 1

        low, high = 1, n
        while low < high:
            mid = (low + high) // 2
            count = 0
            for i in nums:
                # 遍历查看比小于等于 mid 的个数
                if i <= mid:
                    count += 1

            if count > mid:
                high = mid
            else:
                low = mid + 1
        # 返回low和high相等的值
        return low

    def findDuplicate2(self, nums: List[int]) -> int:
        # 快慢指针
        slow, fast = 0, 0
        slow = nums[slow]
        fast = nums[nums[fast]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # 再走 a 步，使得新指针与慢指针重逢
        new_ptr = 0
        while new_ptr != slow:
            new_ptr = nums[new_ptr]
            slow = nums[slow]
        return slow
