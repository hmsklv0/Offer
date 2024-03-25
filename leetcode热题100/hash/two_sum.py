# https://leetcode.cn/problems/two-sum/?envType=study-plan-v2&envId=top-100-liked
# 1. 两数之和

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        processed_nums = {}
        for index in range(len(nums)):
            item = nums[index]
            if (target - item) in processed_nums:
                return [index, processed_nums[target - item]]
            else:
                processed_nums[item] = index

        return [0, 0]

    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        processed_nums = {}
        for index, item in enumerate(nums):
            if (target - item) in processed_nums:
                return [index, processed_nums[target - item]]
            else:
                processed_nums[item] = index

        return [0, 0]

a = Solution()
print(a.twoSum2([2, 7, 11, 15], 9))
