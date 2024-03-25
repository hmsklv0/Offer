class Solution:
    def maxValue(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for j in range(1, n):  # 初始化第一行
            grid[0][j] += grid[0][j - 1]
        for i in range(1, m):  # 初始化第一列
            grid[i][0] += grid[i - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += max(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]

    def maxValue2(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # dp初始化 & 或者使用numpy初始化
        dp = []
        for i in range(0, m):
            dp.append([])
            for j in range(0, n):
                dp[i].append(0)
        dp[0][0] = grid[0][0]

        # 初始化第一行
        for j in range(1, n):
            dp[0][j] = grid[0][j] + dp[0][j - 1]
        # 初始化第一列
        for i in range(1, m):
            dp[i][0] = grid[i][0] + dp[i - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + max(dp[i][j - 1], dp[i - 1][j])
        return dp[-1][-1]


test = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
test2 = [[1, 2, 5], [3, 2, 1]]
solution = Solution()
print(solution.maxValue2(test2))
