# 链表：https://leetcode.cn/problems/longest-substring-without-repeating-characters/solutions/2361797/3-wu-zhong-fu-zi-fu-de-zui-chang-zi-chua-26i5/
# https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/?envType=study-plan-v2&envId=top-100-liked


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 转换为找两个相同的字符
        result, dic = 0, {}
        i = -1
        for j in range(len(s)):
            if s[j] in dic:
                # 出现重复的字符，意味着重新开始计算当前的字串长度
                # 更新左指针
                i = max(dic[s[j]], i)
            dic[s[j]] = j

            result = max(result, j - i)
        return result




