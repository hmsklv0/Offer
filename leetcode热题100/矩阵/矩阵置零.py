# https://leetcode.cn/problems/set-matrix-zeroes/solutions/6594/o1kong-jian-by-powcai/?envType=study-plan-v2&envId=top-100-liked
# O(1)复杂度，将第一列和第一行作为标志位，但是要注意本身有零的情况

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # row array
        # 用集合记录哪些行、哪些列需要置零
        row, array = set(), set()

        row_len = len(matrix)
        array_len = len(matrix[0])
        for i in range(row_len):
            for j in range(array_len):
                if matrix[i][j] == 0:
                    row.add(i)
                    array.add(j)
        for i in row:
            # 修改行数据
            for j in range(array_len):
                matrix[i][j] = 0
        for j in array:
            # 修改列数据
            for i in range(row_len):
                matrix[i][j] = 0


matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
a = Solution()
a.setZeroes(matrix)
print(matrix)
