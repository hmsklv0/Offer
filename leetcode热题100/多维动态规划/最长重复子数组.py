# 题解 多维动态规划
# https://programmercarl.com/0718.%E6%9C%80%E9%95%BF%E9%87%8D%E5%A4%8D%E5%AD%90%E6%95%B0%E7%BB%84.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        res = 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            # 第一列初始化
            if nums1[i] == nums2[0]:
                dp[i][0] = 1
                res = 1
        for j in range(n):
            # 第一行初始化
            if nums1[0] == nums2[j]:
                dp[0][j] = 1
                res = 1
        for i in range(1, m):
            for j in range(1, n):
                # 递推公式
                if nums1[i] == nums2[j]:
                    print(i, j)

                    dp[i][j] = dp[i - 1][j - 1] + 1
                    res = max(res, dp[i][j])

        print(dp)
        return res

    def findLength2(self, nums1: List[int], nums2: List[int]) -> int:
        # 代码简化版本
        m = len(nums1)
        n = len(nums2)
        res = 0
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    # 该办法不需要考虑初始化问题
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    res = max(res, dp[i][j])

        print(dp)
        return res


a = Solution()
n1 = [1, 2, 3, 2, 8]
n2 = [5, 6, 1, 4, 7]
print(a.findLength(n1, n2))
print(a.findLength2(n1, n2))
