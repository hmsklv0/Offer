import string


class Solution:
    def decodeString(self, s: str) -> str:
        # 双栈组合解决，没遇到一个新的[，数组中新开一个数组对象进行处理
        stack_str = [[]]
        stack_num = [[]]

        for i in range(len(s)):

            if s[i] == '[':
                # 开始记录最新字符
                stack_str.append([])
                stack_num.append([])
            elif s[i] == ']':
                # 处理当前最顶端字符串，并将其挂载到最新的字符串上
                # print(stack_str)
                # print(stack_num)
                str_item_list = stack_str.pop()
                str_item = ''.join(str_item_list)
                num_str = ''.join(stack_num.pop())
                if num_str == '':
                    num_str = ''.join(stack_num.pop())
                num = int(num_str)

                str_item = str_item * num
                stack_str[-1].append(str_item)

                stack_num.append([])

            elif s[i] in string.ascii_lowercase:
                stack_str[-1].append(s[i])
            elif ord(s[i]) <= ord('9') and ord(s[i]) >= ord('0'):
                if len(stack_num) != 0:
                    stack_num[-1].append(s[i])
                else:
                    stack_num.append([s[i]])

        return ''.join(stack_str.pop())

    def decodeString2(self, s: str) -> str:
        # 利用栈处理多层嵌套问题，将
        # 将 multi, res 组合存放在栈中
        stack = []
        multi, res = 0, ""

        for i in range(len(s)):
            # 想一想，在栈顶如何操作
            # 将当前的[]中的字符乘之前的数字，再加上前缀部分，以此递归

            if s[i] == '[':
                # 将原本的 multi 和 res 入栈，并重新归零
                stack.append((multi, res))
                res, multi = "", 0

            elif s[i] == ']':
                # 处理当前最顶端字符串，并将其挂载到最新的字符串上
                cur_multi, last_res = stack.pop()
                res = last_res + res * cur_multi

            elif s[i] in string.ascii_lowercase:
                res = res + s[i]

            elif ord(s[i]) <= ord('9') and ord(s[i]) >= ord('0'):
                multi = multi * 10 + int(s[i])

        return res

    def decodeString3(self, s: str) -> str:
        stack = []
        multi, res = 0, ""
        # 核心计算方法 res = pre_res + pre_multi * res
        # 栈顶 不看multi,只看res

        for i in range(len(s)):
            if s[i] in string.ascii_lowercase:
                res += s[i]
            elif ord('0') <= ord(s[i]) <= ord('9'):
                multi = multi * 10 + int(s[i])
            elif s[i] == '[':
                stack.append((multi, res))
                multi, res = 0, ""
            elif s[i] == ']':
                # 3[5[ab]]
                # stack 3 ""
                # stack 5 ""
                # 1 ] res = "ab" multi = 0
                # 核心计算方法 res = pre_res + pre_multi * res
                pre_multi, pre_res = stack.pop()
                res = pre_res + pre_multi * res

        return res
