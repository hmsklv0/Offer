from typing import List
# https://leetcode.cn/problems/next-permutation/solutions/479151/xia-yi-ge-pai-lie-by-leetcode-solution/?envType=study-plan-v2&envId=top-100-liked
# 题解

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 这种方法比较狭隘，是错误的，不能考虑到所有情况
        # 如 [1,3,2]
        # 正确回答为 [2,1,3], 而不是 [2,3,1]

        nums_len = len(nums)
        if nums_len == 1:
            return None

        left, right = nums_len - 2, nums_len - 1

        while right > 0:
            for i in range(right - 1, -1, -1):
                if nums[i] < nums[right]:
                    nums[i], nums[right] = nums[right], nums[i]
                    return None
            right = right - 1

        return nums.sort()

    def nextPermutation(self, nums: List[int]) -> None:
        # 下一个排列是怎样 尾端是降序排列，这样就必须找到前一位 a 进行解决，分为两种情况
        # + 有a，交换降序排列中比 a 大的最小的一个元素，从后往前找就可以了
        # + 无a，直接翻转数组
        # 1 寻找 第一对 nums[i]< nums[i+1],交换 小 大, 就能 大 小，为了保证是最小的交换，所以是寻找第一对小大交换，否则在 i+1 ,n 的区间中为一个降序排列，这种交换必然是比原来的要小
        # 2 找到后，寻找 i + 1 ,n 的区间中比 nums[i] 大的值中 的最小值，然后将数组进行逆序，即升序排列

        # 注意：寻找时是从后往前找
        nums_len = len(nums)
        if nums_len == 1:
            return None
        i = nums_len - 2

        #   注意 两个 >=， 非严格降序
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        print(i, nums[i])

        if i >= 0:
            for j in range(nums_len - 1, i, -1):
                print(nums[j])

                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    break

        left, right = i + 1, nums_len - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1



