# https://programmercarl.com/0977.%E6%9C%89%E5%BA%8F%E6%95%B0%E7%BB%84%E7%9A%84%E5%B9%B3%E6%96%B9.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        k = len(nums) - 1
        result = [0 for i in range(k + 1)]
        while left <= right and k >= 0:
            if abs(nums[left]) > abs(nums[right]):
                result[k] = pow(nums[left], 2)
                left += 1
            else:
                result[k] = pow(nums[right], 2)
                right -= 1
            k -= 1
        return result
