# 题解 https://leetcode.cn/problems/first-missing-positive/?envType=study-plan-v2&envId=top-100-liked
# 此题的解题思路在于将原本的数组的索引作为哈希表的键值，如 a[1] = 2, a[0] = 1，做到一一对应，而没有对应的最小整数则为空缺的那一个

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums_len = len(nums)
        for i in range(nums_len):
            # nums[i] 为负数或者大于区间时，没有意义
            # 真正的循环条件时 是当前遍历值有对应的位置可去
            while nums[i] > 0 and nums[i] <= nums_len and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(nums_len):
            if nums[i] != i + 1:
                return i + 1
        return nums_len + 1

    def firstMissingPositive2(self, nums: list[int]) -> int:
        # 修改循环写法
        nums_len = len(nums)
        i = 0
        while i < nums_len:
            # nums[i] 为负数或者大于区间时，没有意义
            # 真正的循环条件时 是当前遍历值有对应的位置可去
            if nums[i] > 0 and nums[i] <= nums_len and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1

        for i in range(nums_len):
            if nums[i] != i + 1:
                return i + 1
        return nums_len + 1


a = Solution()
nums = [3, 4, -1, 1]
print(a.firstMissingPositive2(nums))
