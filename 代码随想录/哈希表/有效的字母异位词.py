import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = collections.Counter(s)
        b = collections.Counter(t)

        if a == b:
            return True
        else:
            return False

    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a = collections.Counter(s)

        for i in range(len(t)):
            if t[i] in a:
                a[t[i]] -= 1
        count = 0
        for _, v in a.items():
            # 避免为负值的情况出现
            if v >= 0:
                count += v
        if count == 0:
            return True
        else:
            return False

    def isAnagram3(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        result = [0 for _ in range(26)]
        for i in s:
            result[ord(i) - ord('a')] += 1
        for j in t:
            result[ord(j) - ord('a')] -= 1
        for u in range(26):
            if result[u] != 0:
                return False
        return True

