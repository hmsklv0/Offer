# 题解 https://leetcode.cn/problems/sliding-window-maximum/solutions/2361228/239-hua-dong-chuang-kou-zui-da-zhi-dan-d-u6h0/?envType=study-plan-v2&envId=top-100-liked
# 使用辅助栈来记录当前窗口移动中的最大值排序，非严格递减
# 一方面保证前面的最大值比后面的最大值先进，也通过队列保证先出

import collections


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # 朴素做法，会超时
        max_w = max(nums[:k])
        maxWindow = [max_w]

        if (len(nums) <= 1):
            return maxWindow
        for i in range(k, len(nums)):
            if nums[i] > max_w:
                max_w = nums[i]
                maxWindow.append(max_w)
            else:
                max_w = max(nums[i - k + 1:i + 1])
                maxWindow.append(max_w)

        return maxWindow

    def maxSlidingWindow2(self, nums: list[int], k: int) -> list[int]:
        # 使用辅助队列解决，队列保持单调递减，从而保证队列的首元素始终为当前窗口的最大值
        if not nums or k == 0:
            return []
        deque = collections.deque()

        # 初始化辅助队列，即整理 [0:k-1]窗口
        for i in range(k):
            # 从队列的后面往前遍历，保证每个添加的元素前不会出现比自己小的数值(deque有值，才会去遍历)
            print(nums[i])
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
        res = [deque[0]]

        # 对[k:len(nums)-1]中的元素进行逐个窗口滑动
        for i in range(k, len(nums)):
            # 添加新元素时，判断队首元素是否应该被popleft出去, 判断条件为 首元素(nums[i-k])是否为最大值(deque[0])
            if deque[0] == nums[i - k]:
                print(deque[0])
                deque.popleft()
            # 保持单调递减的趋势，非严格递减，存在部分元素相等情况，即多个相同值同时为最大值，将多个值保存在队列中，从而popleft时方便弹出
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
            res.append(deque[0])

        return res


a = Solution()
a_l = [1, 3, -1, -3, 5, 3, 6, 7]
a_l2 = [1, -1]
k = 3
print(a.maxSlidingWindow2(a_l2, 1))
