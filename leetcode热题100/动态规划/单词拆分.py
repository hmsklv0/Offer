# https://programmercarl.com/0139.%E5%8D%95%E8%AF%8D%E6%8B%86%E5%88%86.html
# 题解

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        s_len = len(s)

        # 观察dp数组以及下标定义，再观察递推方程
        # 当 dp[j] 和 s[j:i] in wordDict 同时满足时，当前dp[j]是可行的
        dp = [False for _ in range(s_len + 1)]
        dp[0] = True


        for i in range(1, s_len + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True

        return dp[s_len]
