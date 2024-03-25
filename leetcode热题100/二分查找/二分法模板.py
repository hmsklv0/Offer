# 目标值在数组所有元素之前
# 目标值等于数组中某一个元素
# 目标值插入数组中的位置
# 目标值在数组所有元素之后

# 第一种写法 以下的代码中定义 target 是在一个在左闭右闭的区间里，也就是[left, right]
# 详情查看搜索插入位置
# https://leetcode.cn/problems/search-insert-position/solutions/1022541/dai-ma-sui-xiang-lu-che-di-jiang-tou-er-5zs9r/?envType=study-plan-v2&envId=top-100-liked

from typing import List


def searchInsert(nums: List[int], target: int):
    n = len(nums)
    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
