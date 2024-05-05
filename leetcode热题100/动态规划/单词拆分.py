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

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        # 背包问题
        # 1 表明 以 第 i 个字符结尾的字符串能否被拼接出来
        dp = [False for _ in range(len(s) + 1)]

        # 2 递推公式
        # 如果确定dp[j] 是true，且 [j, i] 这个区间的子串出现在字典里
        # 那么dp[i]一定是true。（j < i ）。
        # if dp[j] and s[j:i] in wordDict:
        #     dp[i] = True
        # if wordDict[j] == s[i - len(wordDict[j]) : i + 1]:
        #     dp[i] = dp[i - len(wordDict[j])]

        # 3 初始化
        dp[0] = True

        # 4 遍历顺序(不能采用外物品的形式,外物品,适用预只在乎组合起来能否满足,不在乎排列顺序-强调求排列数时强调物品之间顺序。
        # 比如硬币, 我们只要最后总数满足情况即可,2+2+1, 2+1+2是一样的情况,但是外物品只能做到 1 2 2这种情况 2 2 1不能 2 1 2
        # 例子 "apple" + "apple" + "pen"
        # 而本题其实我们求的是排列数，为什么呢。 拿 s = "applepenapple", wordDict = ["apple", "pen"] 举例。
        # "apple", "pen" 是物品，那么我们要求 物品的组合一定是 "apple" + "pen" + "apple" 才能组成 "applepenapple"。
        # 外遍历 背包
        # 内遍历 物品
        for i in range(1, len(s) + 1):
            # 实际上的字符是从0开始排序的，
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[-1]
