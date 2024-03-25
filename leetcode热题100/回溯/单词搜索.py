# https://leetcode.cn/problems/word-search/solutions/2361646/79-dan-ci-sou-suo-hui-su-qing-xi-tu-jie-5yui2/?envType=study-plan-v2&envId=top-100-liked
# 与岛屿问题类似
# 链接为相似思路题解

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        cur_word = list(word)

        visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.dfs(board, i, j, cur_word, visited) is True:
                        return True
        return False

    def dfs(self, board: List[List[str]], r: int, c: int, cur_word: list[str], visited: List[List[int]]) -> bool:
        # 终止条件
        if len(cur_word) == 0:
            # 结束判断
            return True
        if not self.isArea(board, r, c):
            # 是否在范围内
            return False
        if board[r][c] != cur_word[0] or visited[r][c] == 1:
            # 是否 匹配当前字符和 是否被访问过
            return False

        # 需要进一步迭代时，设置当前节点已被访问
        visited[r][c] = 1
        next_word = cur_word[1:]

        a = self.dfs(board, r + 1, c, next_word, visited)
        b = self.dfs(board, r - 1, c, next_word, visited)
        x = self.dfs(board, r, c + 1, next_word, visited)
        y = self.dfs(board, r, c - 1, next_word, visited)

        visited[r][c] = 0

        if a or b or x or y:
            return True
        else:
            return False

    def isArea(self, board: List[List[str]], r: int, c: int):
        return 0 <= r < len(board) and 0 <= c < len(board[0])
