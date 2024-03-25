class Solution:
    def findNumberIn2DArray(self, matrix: list[list[int]], target: int) -> bool:
        def helper(nums: list[int], target):
            i, j = 0, len(nums) - 1
            while i <= j:
                m = (i + j) // 2
                if nums[m] < target:
                    i = m + 1
                elif nums[m] > target:
                    j = m - 1
                elif nums[m] == target:
                    return m

        for list_i in matrix:
            result = helper(list_i, target)
            if result is not None:
                return True
        return False
    def findNumberIn2DArray2(self, matrix: list[list[int]], target: int) -> bool:
        n = len(matrix) - 1
        if n != -1:
            m = len(matrix[0]) - 1
            i, j = 0, m
            while i <= n and j >= 0:
                if target < matrix[i][j]:
                    j -= 1
                elif target > matrix[i][j]:
                    i += 1
                elif target == matrix[i][j]:
                    return True
        return False

list1 = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
list2 = [[-5]]
solution = Solution()
print(solution.findNumberIn2DArray2(list2, -5))