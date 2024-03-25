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
