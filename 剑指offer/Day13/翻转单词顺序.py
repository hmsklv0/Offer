class Solution:
    def reverseWords(self, s: str) -> str:
        list_s = s.split(' ')
        # print(list_s)
        s_result_list = []
        len_s_list = len(list_s)
        i = len_s_list - 1
        while i >= 0:
            if list_s[i] == '':
                list_s.pop(i)
            else:
                s_result_list.append(list_s.pop(i))
            i -= 1

        return ' '.join(s_result_list)

    def reverseWords2(self, s: str) -> str:
        s = s.strip()

        i = j = len(s) - 1

        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ':
                # 搜索首个空格
                i -= 1
            # 添加单词
            res.append(s[i + 1: j + 1])
            # 跳过单词间空格
            while s[i] == ' ':
                i -= 1
            # j 指向下个单词的尾字符
            j = i

        return ' '.join(res)



str1 = "the sky is blue"
str2 = "  hello world!  "
str3 = "a good   example"
str_list = [str1, str2, str3]
solu = Solution()
for i in range(3):

    print(solu.reverseWords(str_list[i]))

