class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 定义 dp[j] 为以 s[j] 为结尾的最长字符串长度
        # 因此 dp 动态规划表的长度为 len(s)
        # 因此 每个字符只用管前面的字符串里面有没有自己的重复字母，就能得到当前字母的最长字符串，因为其前一个字符字串一定是 能得到最长的不重复的字串
        dp = [0 for i in range(len(s))]
        # 字典(哈希表)记录字符最近出现的索引
        dic = {}

        for j in range(len(s)):
            # 索引存取
            i = dic.get(s[j], -1)
            dic[s[j]] = j

            # 动态规划表更新
            if dp[j - 1] < j - i:
                dp[j] = dp[j - 1] + 1
            elif dp[j - 1] >= j - i:
                dp[j] = j - i

        return max(dp) if len(dp) != 0 else 0

    def lengthOfLongestSubstring2(self, s: str) -> int:
        # 字典(哈希表)记录字符最近出现的索引
        dic = {}
        res = tmp = 0

        for j in range(len(s)):
            # 索引存取
            i = dic.get(s[j], -1)
            dic[s[j]] = j

            # 动态规划表更新 dp[j - 1] -> dp[j]
            if tmp < j - i:
                tmp = tmp + 1
            elif tmp >= j - i:
                tmp = j - i
            res = max(res, tmp) # max(dp[j - 1], dp[j])
        return res


st = "abcabcbb"
so = Solution()
print(so.lengthOfLongestSubstring(st))