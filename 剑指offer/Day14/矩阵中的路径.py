class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def dfs(i, j, k):
            # 边界问题
            if not (0 <= i < len(board)) or not (0 <= j < len(board[0])) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            board[i][j] = ''
            # 四个方向都去试一试
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            # 深度搜索完后，将当前矩阵元素置为原来的值（赋空值，代表此元素已被访问，后面修改回原值，代表回溯后需要表明该元素没被访问）
            board[i][j] = word[k]
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
