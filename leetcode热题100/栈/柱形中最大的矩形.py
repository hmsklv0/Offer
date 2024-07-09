# https://leetcode.cn/problems/largest-rectangle-in-histogram/solutions/142012/bao-li-jie-fa-zhan-by-liweiwei1419/?envType=study-plan-v2&envId=top-100-liked
# 单调栈总结

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 核心思想
        # 只要是遇到了当前柱形的高度比它上一个柱形的高度严格小的时候，
        # 一定可以确定它之前的某些柱形的最大宽度
        # 通过递增单调栈，快速计算当前高度的柱体对应的结果
        # 0 1 2 3 4 3 2 1 0

        # 对应哨兵 0
        stack = [0]
        res = 0
        # 两个哨兵节点
        # 1 左边的柱形（第 1 个柱形）由于它一定比输入数组里任何一个元素小，
        # 它肯定不会出栈，因此栈一定不会为空；可以一直比较，让所有的元素入栈
        # 2 右边的柱形（第 2 个柱形）也正是因为它一定比输入数组里任何一个元素小，
        # 它会让所有输入数组里的元素出栈（第 1 个哨兵元素除外）。
        # 从而做到对每个柱体进行面积计算

        heights = [0] + heights + [0]
        size = len(heights)

        for i in range(1, size):
            # 当出现小于当前栈顶元素的情况时，需要计算面积
            while heights[i] < heights[stack[-1]]:
                # 该 while 循环的逻辑为，为保持单调递增，因此将当前元素 heights[i] 添加进栈时
                # 需要将大于当前元素的栈顶元素弹出
                # 在弹出的过程中，保证了弹出元素 stack.pop() 大于当前元素
                #
                # 面积计算公式 heights[stack.pop()] * (i - stack[-1] - 1)
                # 注意：弹出元素和当前元素之间均大于或等于stack.pop()
                # 注意：(i - stack[-1] - 1)

                # cur_width = i - stack[-1] -1
                # 计算原理是什么
                # 根据单调栈的原理，
                # 1 如果栈内元素a小于某个柱体b，那么在那个柱体时元素a一定会被pop出去
                # 如果元素a没有被pop出去，那么代表中间的所有高度都是大于元素a
                # 2 同时可以注意到，被pop出去的元素都大于b，因此将主体b添加进栈时
                # 因此。如果b和a之间有元素，那么元素都是大于b和a的。
                # 3 根据单调栈的原理，在b之后添加的元素同样会大于b，因此在将要弹出b时，
                # 计算b的宽度，是从当前节点计算到a柱体，
                cur_height = heights[stack.pop()]

                cur_width = i - stack[-1] - 1
                res = max(res, cur_width * cur_height)

            stack.append(i)
        return res
