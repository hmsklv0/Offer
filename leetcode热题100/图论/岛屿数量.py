from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid: list[list[str]], r: int, c: int):
        # 判断 base case
        # 如果坐标 (r, c) 超出了网格范围，直接返回
        if not self.inArea(grid, r, c):
            return
        # 避免重复访问
        # 0 海洋格子
        # 1 陆地格子 未遍历过
        # 2 陆地格子 已遍历过

        # 表示为 grid[r][c] == 0 or 2，如果碰到海洋或者已经遍历过的格子，立即返回
        if grid[r][c] != '1':
            return

        # 将当前未被遍历的格子标记为 [已遍历过]
        grid[r][c] = '2'

        # 访问上下左右四个相邻节点
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r, c + 1)
        self.dfs(grid, r, c - 1)

    def inArea(self, grid: list[list[str]], r: int, c: int) -> bool:
        return 0 <= r and r < len(grid) and 0 <= c and c < len(grid[0])


