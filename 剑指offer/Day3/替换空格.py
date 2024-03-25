class Solution:
    def replaceSpace(self, s: str) -> str:
        if s == '':
            return ''
        # 内存开销大
        s2 = ''
        for i in range(len(s)):
            if s[i] == ' ':
                s2 = s2 + '%20'
            else: s2 = s2 + s[i]
        return s2

        # # 空格索引
        # space_index = []
        # for i in range(len(s)):
        #     if i == ' ':
        #         space_index.append(i)
        # # 空格切片
        # s_slices = s.split()
        # s2 = ''
        # # 空格替换%20，拼接
        # for i in range(len(space_index)):
        #     s2 = s2 + ''

    def replaceSpace4(self, s: str) -> str:
        # 修改字符串为列表，降低内存开销
        if s == '':
            return ''
        s2 = []
        for i in range(len(s)):
            if s[i] == ' ':
                s2.append('%20')
            else:
                s2.append(s[i])
        return ''.join(s2)

    def replaceSpace2(self, s: str) -> str:
        s_slices = s.split()
        return '%20'.join(s_slices)
        # 空格很多的时候，不行
    def replaceSpace3(self, s: str) -> str:
        return s.replace(' ', '%20')
solution = Solution()
s = '1 2 3 4 5 67 8'
print(solution.replaceSpace(s))