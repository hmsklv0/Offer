class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        def helper(nums: list[int], target: int):
            i, j = 0, len(nums) - 1
            while i <= j:
                m = (i + j) // 2
                if nums[m] <= target:
                    i = m + 1
                else:
                    j = m - 1
            return i

        return list(range(helper(nums, target - 1), helper(nums, target)))

solution = Solution()
t = [1, 2, 2, 3, 4, 5]
print(solution.targetIndices(t, 6))