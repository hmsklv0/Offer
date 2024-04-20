# https://leetcode.cn/problems/sort-colors/solutions/437968/yan-se-fen-lei-by-leetcode-solution/
# 题解
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 根据题目中的提示，我们可以统计出数组中 0,1,20, 1, 20,1,2 的个数，再根据它们的数量，重写整个数组。
        a, b, c = 0, 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                a += 1
            elif nums[i] == 1:
                b += 1
            elif nums[i] == 2:
                c += 1
        for i in range(a):
            nums[i] = 0
        for i in range(a, a + b):
            nums[i] = 1
        for i in range(a + b, a + b + c):
            nums[i] = 2

    def sortColors2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 双指针解决问题，p0用于交换0，p1用于交换1
        # 时间复杂度 O(n)，空间复杂度 O(1)

        # 难点，指针移动条件，即 i为1 ，p1移动1
        # i为0，p1和p0都移动1

        n = len(nums)
        p0, p1 = 0, 0
        for i in range(n):
            if nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                if p0 < p1:
                    # 如果 p0 < p1，那么p0位置原本的1将会被交换至i处，因此需要额外交换一次
                    nums[i], nums[p1] = nums[p1], nums[i]
                p0 += 1
                p1 += 1

    def sortColors3(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 双指针解决问题，p0用于交换0，p2用于交换2
        # 时间复杂度 O(n)，空间复杂度 O(1)

        # 难点，指针移动条件，即 nums[i] 为0 ，p0移动1
        # nums[i] 为2，p2 移动1
        # i 和 p0 中间为1
        # p0 之前全为 0
        # p2 之后全为 2
        # 特殊情况处理，nums[i] 和 p2 交换完成后，需要重新判断是否为2
        # 并且判断是否为0

        n = len(nums)
        p0, p2 = 0, n-1
        i = 0
        while i < p2:
            while i <= p2 and nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1

            i += 1


