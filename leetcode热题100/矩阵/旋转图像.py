# 题解：https://leetcode.cn/problems/rotate-image/solutions/1228078/48-xuan-zhuan-tu-xiang-fu-zhu-ju-zhen-yu-jobi/?envType=study-plan-v2&envId=top-100-liked
# 思路：原地修改的思路
# 思路：修改思路图可见题解的解法2，主要思想为一层层修改，层数为 n//2, 偶数为两倍，奇数-1后再/2
# 思路：而在每层的修改动作，一次为四个点一起修改，修改动作有 每层小正方形的边长 - 1，每个小正方形相隔2
# 思路：
# 思路：


class Solution:
    def rotate(self, matrix: list[list[int]]) -> list[list[int]]:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 借助辅助矩阵
        new_matrix = []

        for i in range(len(matrix)):
            new_matrix.append([0 for j in range(len(matrix[0]))])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                new_matrix[j][-i - 1] = matrix[i][j]
        return new_matrix

    def rotate2(self, matrix: list[list[int]]) -> None:
        array_len = len(matrix)

        # 计算旋转层数
        layer = array_len // 2

        # 每层选择次数
        count = array_len - 1

        for i in range(layer):
            # 每层的修改起点为顶角，(i,i)
            row, array = 0 + i, 0 + i
            for j in range(count):
                tmp = matrix[row][array]
                matrix[row][array] = matrix[-array - 1][row]
                matrix[-array - 1][row] = matrix[-row - 1][-array - 1]
                matrix[-row - 1][-array - 1] = matrix[array][-row - 1]
                matrix[array][-row - 1] = tmp
                # 继续下一层
                row += 1
            count -= 2
            if count <= 0:
                break


a = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(a.rotate2(matrix))
print(matrix)
