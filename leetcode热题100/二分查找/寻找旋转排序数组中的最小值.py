# https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/solutions/698479/xun-zhao-xuan-zhuan-pai-xu-shu-zu-zhong-5irwp/?envType=study-plan-v2&envId=top-100-liked
# 我们考虑数组中的最后一个元素 xxx：
# 在最小值右侧的元素（不包括最后一个元素本身），它们的值一定都严格小于 x；
# 而在最小值左侧的元素，它们的值一定都严格大于 x。
# 因此，我们可以根据这一条性质，通过二分查找的方法找出最小值。

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            # 即使在全是左侧的升序排列，仍然会趋近最低点，
            # 更何况，nums[right]会比左侧的升序排列整体偏低
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]

    def findMin2(self, nums: List[int]) -> int:
        # 错误做法
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            # 因为在右侧的升序排列，这个关系也成立，但是不会趋近最低点
            if nums[mid] > nums[left]:
                left = mid + 1
            else:
                right = mid
        return nums[right]

a = Solution()
list1 = [3, 4, 5, 1, 2]
list2 = [4, 5, 6, 7, 0, 1, 2]
list3 = [3, 1, 2]
print(a.findMin(list3))
