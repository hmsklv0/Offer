# 题解: https://leetcode.cn/problems/search-a-2d-matrix-ii/solutions/118335/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-5-4/?envType=study-plan-v2&envId=top-100-liked
# 主要解法为从右上角进行遍历，大于target，往左走；小于target，往下走

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # 失败了
        m = len(matrix)
        n = len(matrix[0])
        if matrix[0][0] == target:
            return True
        elif target < matrix[0][0] or matrix[-1][-1] < target:
            return False
        flag = 0
        row_index, array_index = 0, 0
        for i in range(0, m):
            if matrix[i][0] > target:
                flag = 1
                row_index = i - 1
                print("row_index", row_index)
                break
            # 修复相等的情况判定
            elif matrix[i][0] == target:
                return True
        if flag == 0:
            row_index = i

        flag = 0
        for j in range(0, n):
            if matrix[0][j] > target:
                flag = 1
                array_index = j - 1
                print("array_index", array_index)

                break
            # 修复相等的情况判定
            elif matrix[0][j] == target:
                return True
        if flag == 0:
            array_index = j

        # +1 修复原本不到边界的问题

        for i in range(row_index + 1):
            if matrix[i][array_index] == target:
                return True
        # +1 修复原本不到边界的问题
        for j in range(array_index + 1):
            if matrix[row_index][j] == target:
                return True
        return False

    def searchMatrix2(self, matrix: list[list[int]], target: int) -> bool:
        # 失败了
        m = len(matrix)
        n = len(matrix[0])
        if matrix[0][0] == target:
            return True
        elif target < matrix[0][0] or matrix[-1][-1] < target:
            return False

        # 从顶角开始判断，因为顶角代表着区域最大值
        t = min(m, n)
        if m == n:
            flag = 0
        elif m < n:
            flag = 1
        else:
            # m > n
            flag = 2

        index = 1
        # 通过顶点进行判断
        while index <= t:
            print(matrix[-index][-index])
            if matrix[-index][-index] < target:
                break
            elif matrix[-index][-index] == target:
                return True
            else:
                index += 1
        # 特殊判断
        if index > t:
            for i in range(n):
                if matrix[0][i] == target:
                    return True
            for j in range(m):
                if matrix[j][0] == target:
                    return True

        else:
            index = index - 1
            print(index)
            print(n - index - 1)
            print(m - index - 1)
            for i in range(n - index):
                if matrix[m - index][i] == target:
                    return True
            for j in range(m - index):
                if matrix[j][n - index] == target:
                    return True

        return False

    def searchMatrix3(self, matrix: list[list[int]], target: int) -> bool:
        # 失败，利用右轴进行遍历
        m = len(matrix)
        n = len(matrix[0])
        if matrix[0][0] == target:
            return True
        elif target < matrix[0][0] or matrix[-1][-1] < target:
            return False

        for i in range(m):
            print(matrix[i][n - 1])
            if matrix[i][n - 1] > target:
                break
            elif matrix[i][n - 1] == target:
                return True
        row_index = i
        for j in range(n):
            if matrix[row_index][j] == target:
                return True
        return False

    def searchMatrix4(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        if matrix[0][0] == target:
            return True
        elif target < matrix[0][0] or matrix[-1][-1] < target:
            return False
        row_index, array_index = 0, n - 1

        while row_index < m and array_index >= 0:
            print(matrix[row_index][array_index])
            if matrix[row_index][array_index] > target:
                array_index -= 1
            elif matrix[row_index][array_index] < target:
                row_index += 1
            else:
                # matrix[row_index][array_index] == target
                return True
        return False


a = Solution()
matrix = [
    [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    , [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    , [[-1, 3]]
    , [[1, 4], [2, 5]]
    , [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    , [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [11, 13, 15, 17, 19], [12, 14, 16, 18, 20], [21, 22, 23, 24, 25]]
    , [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
    , [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
]
target = [20, 5, 3, 5, 19, 13, 3, 15]

# print(a.searchMatrix(matrix, target))
for wi in range(len(target)):
    # if wi == 5:
    print("第{}次\n".format(wi), a.searchMatrix4(matrix[wi], target[wi]))
