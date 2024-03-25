# 题解1 https://leetcode.cn/problems/spiral-matrix/solutions/2362055/54-luo-xuan-ju-zhen-mo-ni-qing-xi-tu-jie-juvi/?envType=study-plan-v2&envId=top-100-liked
# 思路：借助四个上下左右的循环，解决问题

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        if bottom == 0:
            return matrix[0]
        elif right == 0:
            return [i[0] for i in matrix]
        res = []
        while True:
            # left to right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            if top > bottom:
                # 终止打印条件，上界突破下界
                break

            # top to bottom
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if left > right:
                # 终止打印条件，左边界突破右边界
                break

            # right to left
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            if top > bottom:
                # 终止打印条件，上界突破下界
                break

            # bottom to top
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:
                # 终止打印条件，左边界突破右边界
                break
        return res


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = Solution()
print(a.spiralOrder(matrix))
