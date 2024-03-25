# https://leetcode.cn/problems/search-a-2d-matrix/solutions/688117/sou-suo-er-wei-ju-zhen-by-leetcode-solut-vxui/?envType=study-plan-v2&envId=top-100-liked
# 两次二分查找
# 或者拼接数组，一次二分查找
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binarySearch(nums: List[int], cur_target):
            # [left, right)
            left, right = 0, len(nums)

            while left < right:
                mid = (left + right) // 2
                if nums[mid] == cur_target:
                    return mid
                elif nums[mid] > cur_target:
                    right = mid
                else:
                    left = mid + 1
            return left - 1

        head_matrix = [row[0] for row in matrix]
        print(head_matrix)
        row_num = binarySearch(head_matrix, target)
        print(row_num)

        if 0 <= row_num < len(head_matrix):
            column_num = binarySearch(matrix[row_num], target)
            print(column_num)
            if 0 <= column_num < len(matrix[0]):
                return True
        return False


lnums = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
nums2 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]

a = Solution()
print(a.searchMatrix(lnums, 3))
