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

    def canJump2(self, nums: List[int]) -> bool:

        # 核心思想:逐个遍历, 计算 cover 能否覆盖到最后的终点
        # cover = nums[i] + i
        # 如果cover不能抵达当前索引,返回False
        cover = 0
        for i in range(len(nums)):
            if i > cover:
                return False
            cover = max(cover, nums[i] + i)
            if cover >= len(nums) - 1:
                return True
        return True
