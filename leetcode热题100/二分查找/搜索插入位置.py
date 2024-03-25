# https://leetcode.cn/problems/search-insert-position/solutions/1022541/dai-ma-sui-xiang-lu-che-di-jiang-tou-er-5zs9r/?envType=study-plan-v2&envId=top-100-liked
# 思路：正经思路，左右分别查找边界
# 思路2：查找 target 和 target+1 的左边界
# 思路2：查找到中心位置后
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if target > nums[left]:
            return left + 1
        else:
            return left

    def searchInsert2(self, nums: List[int], target: int) -> int:
        # [left, right] 左闭右闭区间
        # 区别1 right 初始值
        left, right = 0, len(nums) - 1

        # 区别2 循环结束条件
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                # 区别3 right赋值
                right = mid - 1
        # 区别4 返回值
        return right + 1
#         // 分别处理如下四种情况
#         // 目标值在数组所有元素之前  [0, -1]
#         // 目标值等于数组中某一个元素  return middle;
#         // 目标值插入数组中的位置 [left, right]，return  right + 1
#         // 目标值在数组所有元素之后的情况 [left, right]，因为是右闭区间，所以 return right + 1


    def searchInsert3(self, nums: List[int], target: int) -> int:
        # [left, right) 左闭右开区间
        # 注意 right 为 len(nums)
        # 定义target在左闭右开的区间里，[left, right)  target
        # 区别1 right 初始值
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                # 区别2 right赋值
                right = mid
        # 区别3 返回值
        return right


        # // 分别处理如下四种情况
        # // 目标值在数组所有元素之前 [0,0)
        # // 目标值等于数组中某一个元素 return middle
        # // 目标值插入数组中的位置 [left, right) ，return right 即可
        # // 目标值在数组所有元素之后的情况 [left, right)，因为是右开区间，所以return right

