# https://leetcode.cn/problems/find-all-anagrams-in-a-string/solutions/1123971/zhao-dao-zi-fu-chuan-zhong-suo-you-zi-mu-xzin/?envType=study-plan-v2&envId=top-100-liked
#

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        sorted_p = sorted(p)
        list_index = []
        for i in range(len(s)-len(p) + 1):
            print(i)
            if sorted(s[i:i+len(p)]) == sorted_p:
                list_index.append(i)

        return list_index

    def findAnagrams2(self, s: str, p: str) -> list[int]:
        s_len, p_len = len(s), len(p)

        if s_len < p_len:
            return []

        ans = []
        s_count = [0] * 26
        p_count = [0] * 26
        for i in range(p_len):
            # 这一步是为了做一个列表，统计窗口中的字符次数，按照 26 个字符顺序进行排序
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1

        if s_count == p_count:
            ans.append(0)

        for i in range(s_len - p_len):
            s_count[ord(s[i]) - 97] -= 1
            s_count[ord(s[i + p_len]) - 97] += 1

            if s_count == p_count:
                # 通过比较两个列表list是否相等，来进行判断
                ans.append(i + 1)

        return ans


    def findAnagrams3(self, s: str, p: str) -> list[int]:
        s_len, p_len = len(s), len(p)

        if s_len < p_len:
            return []

        ans = []
        count = [0] * 26
        for i in range(p_len):
            # 0 代表相同
            # >0 s 更多
            # <0 p 更多
            count[ord(s[i]) - 97] += 1
            count[ord(p[i]) - 97] -= 1

        differ = [c != 0 for c in count].count(True)

        if differ == 0:
            ans.append(0)

        for i in range(s_len - p_len):
            # 处理头（处理s[i]的删除对differ的影响 如果s[i]对应的字符次数为等于1，那么删除，不同消除一个，differ - 1）
            # 如果s[i]对应的字符次数为等于0，那么删除，意味着不同增加一个， differ + 1
            # 然后对应的字符次数进行相应的减少
            if count[ord(s[i]) - 97] == 1:  # 窗口中字母 s[i] 的数量与字符串 p 中的数量从不同变得相同
                differ -= 1
            elif count[ord(s[i]) - 97] == 0:  # 窗口中字母 s[i] 的数量与字符串 p 中的数量从相同变得不同
                differ += 1
            count[ord(s[i]) - 97] -= 1

            # 处理尾巴（s[i + p_len]）
            # 如果s[i]对应的字符次数为等于-1，那么增加，意味着不同减少一个， differ -1
            # 如果s[i]对应的字符次数为等于0，那么增加，意味着不同增加一个， differ + 1
            if count[ord(s[i + p_len]) - 97] == -1:  # 窗口中字母 s[i+p_len] 的数量与字符串 p 中的数量从不同变得相同
                differ -= 1
            elif count[ord(s[i + p_len]) - 97] == 0:  # 窗口中字母 s[i+p_len] 的数量与字符串 p 中的数量从相同变得不同
                differ += 1
            count[ord(s[i + p_len]) - 97] += 1

            if differ == 0:
                # 循环实际开始的子字符串对比是从1开始的，从0开始的一开始在外面进行了
                ans.append(i + 1)

        return ans