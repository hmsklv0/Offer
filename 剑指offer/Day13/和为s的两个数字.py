class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            num_sum = nums[i] + nums[j]
            if num_sum < target:
                i += 1
            elif num_sum > target:
                j -= 1
            else:
                # num_sum == target:
                return [nums[i], nums[j]]
        return []