# https://leetcode.cn/problems/daily-temperatures/solutions/868874/yi-pian-ti-jie-gao-ding-dan-diao-zhan-we-2pkf/?envType=study-plan-v2&envId=top-100-liked
# 单调栈问题总结

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 记录数值和位置
        temperature_stack = []
        answer = [0 for i in range(len(temperatures))]
        for i in range(len(temperatures) - 1):
            if temperatures[i] < temperatures[i + 1]:
                # 当递增时，考虑两种情况，非空栈和空栈
                if not temperature_stack:
                    answer[i] = 1
                else:
                    # 当前的
                    answer[i] = 1
                    num, num_index = temperature_stack[-1]
                    while num < temperatures[i + 1]:
                        answer[num_index] = 1 + i - num_index
                        temperature_stack.pop()
                        if temperature_stack:
                            num, num_index = temperature_stack[-1]
                        else:
                            break

            else:
                temperature_stack.append((temperatures[i], i))
        return answer

    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
        # 根据单调栈原理优化
        # 仅记录位置

        # 单调递减 栈，根据当前元素和栈顶元素判断，是否进行栈pop操作
        stack = []
        answer = [0 for i in range(len(temperatures))]
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1]:
                stack_index = stack.pop()
                answer[stack_index] = i - stack_index

            stack.append(i)
        return answer

    def dailyTemperatures3(self, temperatures: List[int]) -> List[int]:
        # 使用一个辅助栈，记录气温递减的状态，使用单调递减栈解决
        stack = []

        res = [0 for i in range(len(temperatures))]
        stack = [0]
        for i in range(1, len(temperatures)):
            # 维护一个单调递减栈（非严格递减栈），如果出现大于栈顶元素的 temperatures[i]，相等不用变化，直接添加进栈
            # 那么将循环遍历，将栈顶元素逐个弹出，然后计算相应的气温升高日期
            # 直至栈顶元素大于 temperatures[i]，或者栈为空，然后将 temperatures[i] 的索引添加至单调递减栈
            while len(stack) != 0 and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        return res
