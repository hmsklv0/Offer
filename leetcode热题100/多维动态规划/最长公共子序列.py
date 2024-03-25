# https://programmercarl.com/1143.%E6%9C%80%E9%95%BF%E5%85%AC%E5%85%B1%E5%AD%90%E5%BA%8F%E5%88%97.html
# 题解
# 相似题目——最长重复子数组
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        # 代表以i-1为结尾的字串 和 以j-1结尾的字串的最长公共子序列
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # 递推公式
        # i, j = 0, 0
        # if text1[i] == text2[j]:
        #     dp[i][j] = dp[i - 1][j - 1] + 1
        # else:
        #     dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]
