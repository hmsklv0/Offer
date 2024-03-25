# 题解 https://leetcode.cn/problems/M1oyTv/solutions/1503503/by-flix-4bcr/
# 最小覆盖字串
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 特殊情况
        if len(s) < len(t):
            return ''

        # 1 创建 t 的字符统计字典
        count_t = collections.Counter(t)
        need = len(t)
        n = len(s)
        min_len = n
        left = 0
        start, end = 0, 0

        # 2 循环查找对应的最小覆盖字串
        for i in range(n):
            # 2.1 移动右侧边界，扩充寻找
            # 有需求的符号对需求need进行处理
            if s[i] in count_t:
                if count_t[s[i]] > 0:
                    need -= 1
                # 所有的符号进行统计处理
                count_t.update({s[i]: -1})
            print(count_t)
            print("need: ", need, end='\t')
            print(s[left:i + 1])

            # 2.2 移动左侧边界，寻找最小覆盖字串
            while need == 0:
                print("收缩")
                # 如果存在最小，只有一个字串,迭代min_len
                if i - left < min_len:
                    min_len = i - left
                    start, end = left, i + 1

                # 1 处理将要滑出的字符
                print("滑出字符", s[left], end='')
                if s[left] in count_t:
                    print("\t需求", end='')
                    # 如果对滑出的字符存在需求
                    if count_t[s[left]] == 0:
                        need += 1
                    count_t.update({s[left]: 1})
                print("")
                print(count_t)
                print("need: ", need, end='\t')
                print(s[left + 1:i + 1])
                # 2 收缩
                left += 1

        return s[start:end]


a = Solution()
s = "cabwefgewcwaefgcf"
t = "cae"
print(a.minWindow(s, t))
