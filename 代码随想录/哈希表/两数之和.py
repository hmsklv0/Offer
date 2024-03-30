from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        processed_nums = {}
        for index in range(len(nums)):
            item = nums[index]
            if (target - item) in processed_nums:
                return [index, processed_nums[target - item]]
            else:
                processed_nums[item] = index

        return [0, 0]
