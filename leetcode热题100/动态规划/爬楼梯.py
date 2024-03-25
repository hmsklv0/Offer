# https://leetcode.cn/problems/climbing-stairs/solutions/854668/dai-ma-sui-xiang-lu-dong-tai-gui-hua-jin-y1hw/?envType=study-plan-v2&envId=top-100-liked
# 题解 动态规划
# 当前步数等于 小一步 和小两步 之和
#             dp[i] = dp[i - 1] + dp[i - 2]


from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        # 递归方法，时间会超标
        res = [0]

        def dfs(pre: List[int], cur_post: int):
            # 终止条件
            if cur_post == 0:
                res[0] += 1
                return
            elif cur_post < 0:
                return

            for i in range(1, 3):
                pre.append(i)
                cur_post -= i
                dfs(pre, cur_post)
                cur_post += i
                pre.pop()

        dfs([], n)
        return res[0]

    def climbStairs2(self, n: int) -> int:
        # 动态规划
        if n <= 2:
            return n

        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            # 当前步数等于 小一步 和小两步 之和
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

    def climbStairs3(self, n: int) -> int:
        # 动态规划 O(1)空间
        if n <= 2:
            return n

        dp1 = 1
        dp2 = 2
        dpi = 0
        for i in range(3, n + 1):
            # 当前步数等于 小一步 和小两步 之和
            dpi = dp1 + dp2
            dp1 = dp2
            dp2 = dpi

        return dpi
