# 题解 动态规划 或者 双指针
# https://programmercarl.com/0647.%E5%9B%9E%E6%96%87%E5%AD%90%E4%B8%B2.html#%E6%80%9D%E8%B7%AF


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        # dp 1 定义 与 3 初始化
        # 1 dp[i][j] 代表 以s[i]开头和以s[j]结尾的字串 是否为回文字串
        dp = [[False for _ in range(n)] for _ in range(n)]
        result = 0

        # 2 递归公式
        # i, j = 0, 0
        # if (s[i] == s[j]):
        #     # 情况一 和 情况二
        #     if j - i <= 1:
        #         result += 1
        #         dp[i][j] = True
        #     # 情况三
        #     elif dp[i + 1][j - 1]:
        #         result += 1
        #         dp[i][j] = True

        for i in range(n - 1, -1, -1):
            for j in range(i, n, 1):
                # 4 遍历顺序所以一定要从下到上，从左到右遍历，这样保证dp[i + 1][j - 1]都是经过计算的
                if s[i] == s[j] and (j - i <= 1 or dp[i + 1][j - 1]):
                    result += 1
                    dp[i][j] = True

        return result

    def countSubstrings2(self, s: str) -> int:
        def extend(cur_s: str, i, j, n):
            # i, j 左右双指针起始位置, n为字符串长度，避免超出边界
            res: int = 0
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
                res += 1

            return res

        # 双指针法
        result: int = 0
        n: int = len(s)
        for i in range(n):
            # 一个元素可以作为中心点，两个元素也可以作为中心点。
            # 遍历到的元素向两边扩散
            result += extend(s, i, i, n)
            result += extend(s, i, i + 1, n)
        return result
