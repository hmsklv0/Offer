# https://programmercarl.com/0072.%E7%BC%96%E8%BE%91%E8%B7%9D%E7%A6%BB.html#%E6%80%9D%E8%B7%AF
# 题解 仔细看题解


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        # dp[i][j] 为 以i-1结尾的字串和 以j-1结尾的字串的最小修改距离
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # 2 递推公式
        # i, j = 0, 0
        # if word1[i - 1] == word2[j - 1]:
        #     dp[i][j] = dp[i - 1][j - 1]
        # else:
        #     # word1 删除 word1[i-1]
        #     dp[i][j] = dp[i - 1][j] + 1
        #     # word1 增加 word2[j-1]
        #     dp[i][j] = dp[i][j - 1] + 1
        #     # word1[i-1] 替换为 word2[j-1]
        #     dp[i][j] = dp[i - 1][j - 1] + 1

        # 3 初始化

        # dp[i][0] ：以下标i-1为结尾的字符串word1，和空字符串word2，最近编辑距离为dp[i][0]。
        # dp[i][0]就应该是i，对word1里的元素全部做删除操作，即：dp[i][0] = i;
        # dp[0][0] = 0
        # dp[0][j]就应该是i，对word1里的元素全部做添加操作，即：dp[0][j] = j;
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        # 4 遍历方式
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # 详情看上面递推公式
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        print(dp)
        return dp[m][n]


a = Solution()
s1 = "horse"
s2 = "ros"
print(a.minDistance(s1, s2))
