class Solution:
    def firstUniqChar(self, s: str) -> str:
        list_1 = []
        dict1 = {}
        # 先统计次数，以及第一次出现
        for i in s:
            count = dict1.setdefault(i, 0)
            if count == 0:
                list_1.append(i)
            dict1[i] = count + 1

        #  遍历第一次出现
        for j in list_1:
            if dict1[j] == 1:
                return j
        return ' '

    def firstUniqChar2(self, s: str) -> str:
        dict1 = {}
        # 先统计次数，以及第一次出现
        for i in s:
            dict1[i] = not i in dict1
        for k, v in dict1.items():
            # if v == True:
            if v:
                return k
        return ' '
