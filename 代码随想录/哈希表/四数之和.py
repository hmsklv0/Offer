from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 保存结果
        res = set()

        # 排序
        nums.sort()

        # 逐个比较
        for i in range(0, len(nums) - 3):
            a = nums[i]
            for j in range(i + 1, len(nums) - 2):
                b = nums[j]
                if nums[i] > target and nums[i] > 0:
                    # 去重
                    break
                if j > i + 1 and nums[j] == nums[j - 1]:
                    # 去重
                    continue
                left, right = j + 1, len(nums) - 1
                while left < right:
                    c, d = nums[left], nums[right]
                    if a + b + c + d == target:
                        res.add((a, b, c, d))
                        right -= 1
                        left += 1
                    elif a + b + c + d > target:
                        right -= 1
                    else:
                        left += 1
        return [list(j) for j in res]


nums = [2, 2, 2, 2, 2]
ab = Solution()
print(ab.fourSum(nums, 8))
