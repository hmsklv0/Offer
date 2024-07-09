# https://leetcode.cn/problems/valid-parentheses/solutions/9185/valid-parentheses-fu-zhu-zhan-fa-by-jin407891080/?envType=study-plan-v2&envId=top-100-liked
# 思路：遇到右边括号，栈pop，并进行对比左括号是否正确


class Solution:
    def isValid(self, s: str) -> bool:
        # 可用字典对辅助队列进行优化
        stack = []
        str_left = ['(', '{', '[']

        str_right = [')', '}', ']']

        for i in s:
            if i in str_left:
                stack.append(i)
            else:
                # if i in str_right
                index = str_right.index(i)
                if str_left[index] != stack.pop():
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

    def isValid2(self, s: str) -> bool:

        stack = []
        dic = {'{': '}', '[': ']', '(': ')'}

        # str_right = [')', '}', ']']
        if len(s) % 2 == 1:
            return False
        for i in range(len(s)):
            if s[i] in dic:
                stack.append(s[i])
            else:
                # 如果当前栈为空，说明根本没有左括号可以匹配
                # 当遇到右括号时，栈弹出栈顶元素，判断左括号是否和栈顶元素配对
                if len(stack) == 0 or s[i] != dic[stack.pop()]:
                    return False

        # "(()()" 避免出现尾部字符匹配，而前部分字符没有匹配项的情况
        if len(stack) == 0:
            return True
        else:
            return False
