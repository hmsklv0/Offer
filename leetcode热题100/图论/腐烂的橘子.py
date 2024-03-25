# 递归思路是一个很差劲的思路，即DFS，该题应采用广度优先搜索的方法
# 题解 https://leetcode.cn/problems/rotting-oranges/solutions/129831/li-qing-si-lu-wei-shi-yao-yong-bfsyi-ji-ru-he-xie-/?envType=study-plan-v2&envId=top-100-liked
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 广度优先搜索
        # 1 统计腐烂橘子，方便后续遍历；统计新鲜橘子数目
        # 2 对腐烂橘子进行扩散，看多久不能继续扩散，扩散轮数即腐烂时间
        # 3 如果新鲜橘子数目归零，那么返回扩散轮数

        self.fresh_count = 0
        rotten_queue = []

        # 1 统计腐烂橘子，方便后续遍历；统计新鲜橘子数目
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == 2:
                    rotten_queue.append((i, j))
                elif grid[i][j] == 1:
                    self.fresh_count += 1

        # 2 对腐烂橘子进行扩散，看多久不能继续扩散，扩散轮数即腐烂时间
        min_minutes = 0
        while rotten_queue:
            queue_len = len(rotten_queue)

            for i in range(queue_len):
                r, c = rotten_queue[i]
                self.expand(grid, r, c, rotten_queue)
                # 扩散操作: 向四周扩散
                # 1 并将新腐烂的橘子加入队列
                # 2 将腐烂橘子标记为已经遍历过
                pass

            min_minutes += 1

        # 3 如果新鲜橘子数目归零，那么返回扩散轮数
        if self.fresh_count == 0:
            return min_minutes
        else:
            return -1

    def expand(self, grid: list[list[int]], r: int, c: int, rotten_queue: list[tuple]):
        expand_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r_change, c_change in expand_list:
            new_r, new_c = r + r_change, c + c_change
            if self.inArea(grid, new_r, new_c):
                if grid[new_r][new_r] == 1:
                    grid[new_r][new_r] = 2
                    rotten_queue.append((new_r, new_c))
                    self.fresh_count -= 1

    def inArea(self, grid: list[list[int]], r: int, c: int) -> bool:
        return 0 <= r and r < len(grid) and 0 <= c and c < len(grid[0])
