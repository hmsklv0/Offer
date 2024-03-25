from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        cover = 0
        for i in range(len(nums)):
            # 注意需要小于等于cover
            if i <= cover:
                cover = max(cover, i + nums[i])
            if cover >= len(nums) - 1:
                return True
        return False
