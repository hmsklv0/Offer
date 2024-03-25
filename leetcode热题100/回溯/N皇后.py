# https://leetcode.cn/problems/n-queens/solutions/399111/51-n-queenshui-su-fa-jing-dian-wen-ti-xiang-jie-by/?envType=study-plan-v2&envId=top-100-liked
# 代码随想录题解
# 主要思路：按照模板来，将循环体的条件设置好，即可得出递归函数需要的参数，然后逐个补全即可
# 真正的思考点如何画树，但是其实很简单，该题相当于循环n层，每层有n个选项，遇到错误选项便回溯

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        pre = [['.' for _ in range(n)] for _ in range(n)]

        def dfs(cur_pre: List[List[str]], cur_r: int) -> None:
            # 终止条件
            if cur_r == len(cur_pre):
                # 添加
                append_pre = []
                for i in range(len(cur_pre)):
                    append_pre.append(''.join(cur_pre[i]))
                res.append(append_pre)

                return

            # 循环体
            for i in range(n):
                if self.isValid(cur_pre, cur_r, i):
                    cur_pre[cur_r][i] = 'Q'
                    dfs(cur_pre, cur_r + 1)
                    cur_pre[cur_r][i] = '.'

        dfs(pre, 0)
        return res

    def isValid(self, cur_pre: List[List[str]], cur_r: int, cur_c: int):
        # 列相同
        for i in range(len(cur_pre)):
            if cur_pre[i][cur_c] == 'Q':
                return False

        # 45° 斜角
        i, j = cur_r - 1, cur_c - 1
        while i >= 0 and j >= 0:
            if cur_pre[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # 135° 斜角
        i, j = cur_r - 1, cur_c + 1
        while i >= 0 and j < len(cur_pre):
            if cur_pre[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        # 所有通过返回True
        return True


a = Solution()
print(a.solveNQueens(4))
