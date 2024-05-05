# 题解 动态规划 或者 双指针
# https://programmercarl.com/0647.%E5%9B%9E%E6%96%87%E5%AD%90%E4%B8%B2.html#%E6%80%9D%E8%B7%AF


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        # dp 1 定义 与 3 初始化
        dp = [[False for _ in range(n)] for _ in range(n)]
        result = [0, (0, 0)]

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
                    dp[i][j] = True
                    if j - i + 1 > result[0]:
                        result[0] = j - i + 1
                        result[1] = (i, j)
        l = result[1][0]
        r = result[1][1]
        return s[l:r + 1]

    def longestPalindrome2(self, s: str) -> str:
        def extend(cur_s: str, i, j, n):
            # i, j 左右双指针起始位置, n为字符串长度，避免超出边界
            res: int = 0
            while i >= 0 and j < n and cur_s[i] == cur_s[j]:
                i -= 1
                j += 1
                res += 2

            return res, i + 1

        # 双指针法
        result: int = 0
        left, right = 0, 0
        n: int = len(s)
        for i in range(n):
            # 一个元素可以作为中心点，两个元素也可以作为中心点。
            # 遍历到的元素向两边扩散
            r1, l = extend(s, i, i, n)
            if r1 - 1 > result:
                result = r1 - 1
                left = l

            r2, l = extend(s, i, i + 1, n)
            if r2 > result:
                result = r2
                left = l

        return s[left:left + result]


    def longestPalindrome3(self, s: str) -> str:
        # 1 dp[i][j] 代表 以s[i]开头和以s[j]结尾的字串 是否为回文字串
        s_len = len(s)
        dp = [[False for _ in range(s_len)] for _ in range(s_len)]

        # 2 递推公式
        # 情况1
        # if s[i] == s[j]:
        #     # 情况1 和 情况2 直接判断为回文字串
        #     if abs(j - i) <= 1:
        #         dp[i][j] = True
        #     else:
        #         # 情况3 根据内部字串是否为回文字串进行判断
        #         dp[i][j] = True if dp[i+1][j-1] is True else False

        # 3 初始化
        dp[0][0] = True
        res = 0
        l, r = 0, 1
        # 4 遍历顺序 从下往上,从左至右 dp[i+1][j-1] -> dp[i][j]
        for j in range(0, s_len):
            for i in range(j, -1, -1):
                # 传统写法1
                # if s[i] == s[j]:
                #     # 情况1 和 情况2 直接判断为回文字串
                #     if abs(j - i) <= 1:
                #         dp[i][j] = True
                #     else:
                #         # 情况3 根据内部字串是否为回文字串进行判断
                #         dp[i][j] = True if dp[i+1][j-1] is True else False
                # 简写2
                if s[i] == s[j] and (j - i <= 1 or dp[i + 1][j - 1] == True):
                    dp[i][j] = True

                # print(dp)
                if dp[i][j] == True:
                    if j - i > res:
                        res = j - i
                        l, r = i, j + 1
        return s[l:r]


a = Solution()
ss = "cbbd"
print(a.longestPalindrome2(ss))
