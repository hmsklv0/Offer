# 情况一：target 在数组范围的右边或者左边，例如数组{3, 4, 5}，target为2或者数组{3, 4, 5},target为6，此时应该返回{-1, -1}
# 情况二：target 在数组范围中，且数组中不存在target，例如数组{3,6,7},target为5，此时应该返回{-1, -1}
# 情况三：target 在数组范围中，且数组中存在target，例如数组{3,6,7},target为6，此时应该返回{1, 1}
#
# 链接：https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/solutions/895599/dai-ma-sui-xiang-lu-34po-shi-wu-hua-de-e-6t89/


from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binaryLeftSearch(nums: List[int], cur_target) -> int:
            # 左边界不动，等在右边界向其靠拢
            # 二分查找，寻找target的左边界leftBorder（不包括target）
            # 如果leftBorder没有被赋值（即target在数组范围的右边，例如数组[3,3],target为4），为了处理情况一

            # 定义 target 在左闭右闭的区间里，[left, right]
            left, right = 0, len(nums) - 1
            # 记录 leftBorder 没有被赋值的情况
            leftBorder = -2

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= cur_target:
                    # 寻找左边界，就要在nums[middle] == target的时候更新right
                    right = mid - 1
                    leftBorder = right
                else:
                    left = mid + 1

            return leftBorder

        def binaryRightSearch(nums: List[int], cur_target) -> int:
            # 右边界不动，等在左边界向其靠拢
            # 二分查找，寻找target的左边界left
            # 二分查找，寻找target的右边界（不包括target）
            # 如果rightBorder为没有被赋值（即target在数组范围的左边，例如数组[3,3]，target为2），为了处理情况一

            left, right = 0, len(nums) - 1
            rightBorder = -2
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= cur_target:
                    left = mid + 1
                    rightBorder = left
                else:
                    right = mid - 1
            return rightBorder

        left = binaryLeftSearch(nums, target)
        right = binaryRightSearch(nums, target)
        if left == -2 or right == -2:
            return [-1, -1]
        if right - left > 1:
            return [left + 1, right - 1]
        return [-1, -1]

    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        # 解法2
        def binary_search(cur_nums: List[int], cur_target: int):
            # 搜寻右边界
            left, right = 0, len(cur_nums)
            while left < right:
                mid = (left + right) // 2
                if cur_nums[mid] > cur_target:
                    right = mid
                elif cur_nums[mid] <= cur_target:
                    left = mid + 1
                else:
                    # cur_nums[mid] == cur_target
                    # 向右边界靠拢
                    pass

            return right

        right_ = binary_search(nums, target)
        left_ = binary_search(nums, target - 1)
        if right_ > 0 and nums[right_ - 1] == target:
            # 判断 target 是否在数组中
            return [left_, right_ - 1]
        else:
            return [-1, -1]

    def searchRange3(self, nums: List[int], target: int) -> List[int]:
        # 解法3
        def binary_search(cur_nums: List[int], cur_target: int):
            # 搜寻右边界
            left, right = 0, len(cur_nums)
            while left < right:
                mid = (left + right) // 2
                if cur_nums[mid] > cur_target:
                    right = mid
                elif cur_nums[mid] <= cur_target:
                    left = mid + 1
                else:
                    # cur_nums[mid] == cur_target
                    # 向右边界靠拢
                    pass

            return right

        def binary_search2(cur_nums: List[int], cur_target: int):
            # 搜寻左边界
            left, right = 0, len(cur_nums)
            while left < right:
                mid = (left + right) // 2
                if cur_nums[mid] >= cur_target:
                    right = mid
                elif cur_nums[mid] < cur_target:
                    left = mid + 1
                else:
                    # cur_nums[mid] == cur_target
                    # 向左边界靠拢
                    pass

            return left

        right_ = binary_search(nums, target)
        left_ = binary_search2(nums, target)
        if right_ > 0 and nums[right_ - 1] == target:
            # 判断 target 是否在数组中
            return [left_, right_ - 1]
        else:
            return [-1, -1]
