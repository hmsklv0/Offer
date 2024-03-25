# https://programmercarl.com/0027.%E7%A7%BB%E9%99%A4%E5%85%83%E7%B4%A0.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# 题解
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 先排序，后移除
        nums.sort()
        n = len(nums)
        start_index = 0
        for i in range(n):
            if nums[i] == val:
                start_index = i
                break

        new_index, step = 0, 0
        for i in range(start_index, n):
            if nums[i] != val:
                new_index = i
                step = i - start_index
                break
            elif nums[i] == val and i == n - 1:
                step = n - start_index
            else:
                continue
        for i in range(start_index, n - step):
            nums[i] = nums[i + step]
        return n - step

    def removeElement2(self, nums: List[int], val: int) -> int:
        # 暴力解法
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == val:
                #  发现需要移除的元素，就将数组集体向前移动一位
                for j in range(i + 1, n):
                    nums[j - 1] = nums[j]
                # 因为下标i以后的数值都向前移动了一位，所以i也向前移动一位
                i -= 1
                # 此时数组的大小-1
                n -= 1
            i += 1
        return n

    def removeElement3(self, nums: List[int], val: int) -> int:
        # 快慢指针
        slow = 0
        # 慢指针指向当前新数组的最后一位
        # 快指针指向新数组的元素
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow

    def removeElement4(self, nums: List[int], val: int) -> int:
        # 相向指针
        left, right = 0, len(nums) - 1
        # 慢指针指向当前新数组的最后一位
        # 快指针指向新数组的元素
        while left <= right:
            # 找左边等于 val 的元素
            while left <= right and nums[left] != val:
                left += 1
            # 找右边不等于 val 的元素
            while left <= right and nums[right] == val:
                right -= 1

            if left < right:
                nums[left] = nums[right]
                left += 1
                right -= 1
        return left


e = [3, 2, 2, 3]
a = Solution()
print(a.removeElement(e, 3))
