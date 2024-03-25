# https://programmercarl.com/0704.%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE.html
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 写法 1 [left, right]
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        # 写法 2 [left, right)
        left, right = 0, len(nums) -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
