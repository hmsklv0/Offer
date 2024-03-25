import math


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        nums_dict = {}
        for i in nums:
            count = nums_dict.setdefault(i, 0)
            nums_dict[i] = count + 1
            # if i in nums_dict:
            #     nums_dict[i] += 1
            # else:
            #     nums_dict.setdefault(i, 1)
        return nums_dict[target] if target in nums_dict else 0


    def search3(self, nums: [int], target: int) -> int:
        def helper(tar):
            i, j = 0, len(nums) - 1
            while i <= j:
                m = (i + j) // 2
                if nums[m] <= tar: i = m + 1
                else: j = m - 1
            return i
        return helper(target) - helper(target - 1)

