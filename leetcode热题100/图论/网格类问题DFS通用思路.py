def dfs(grid: list[list[int]], r: int, c: int):
    # 判断 base case
    # 如果坐标 (r, c) 超出了网格范围，直接返回
    if not inArea(grid, r, c):
        return
    # 避免重复访问
    # 0 海洋格子
    # 1 陆地格子 未遍历过
    # 2 陆地格子 已遍历过

    # 表示为 grid[r][c] == 0 or 2，如果碰到海洋或者已经遍历过的格子，立即返回
    if grid[r][c] != 1:
        return

    # 将当前未被遍历的格子标记为 [已遍历过]
    grid[r][c] = 2

    # 访问上下左右四个相邻节点
    dfs(grid, r + 1, c)
    dfs(grid, r - 1, c)
    dfs(grid, r, c + 1)
    dfs(grid, r, c - 1)


def inArea(grid: list[list[int]], r: int, c: int) -> bool:
    return 0 <= r and r < len(grid) and 0 <= c and c < len(grid[0])
