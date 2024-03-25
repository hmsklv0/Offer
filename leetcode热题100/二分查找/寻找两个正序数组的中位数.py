# https://mp.weixin.qq.com/s/iAFjmYiLMTGwa2ixs_hw8A
# 题解

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 暴力解法
        nums = nums1 + nums2
        nums.sort()
        len_nums = len(nums)
        if len_nums % 2 == 1:
            return nums[len_nums // 2]
        else:
            return (nums[len_nums // 2] + nums[len_nums // 2 - 1]) / 2

    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        # 1.B[j−1] ≤ A[i] && A[i−1] ≤ B[j] 说明i和j左侧的元素都小于等于右侧，这一组i和j是我们想要的。
        # 2.A[i] < B[j−1] 说明i对应的元素偏小了，i应该向右侧移动。
        # 3.A[i−1] > B[j] 说明i-1对应的元素偏大了，i应该向左侧移动。
        m = len(nums1)
        n = len(nums2)

        # 如果m更大，则交换数组
        if m > n:
            return self.findMedianSortedArrays2(nums2, nums1)

        left = 0
        right = m
        mid = (m + n + 1) // 2
        while left <= right:
            # 这里的i就是原来的mid
            i = (left + right) // 2
            j = mid - i

            if i < right and nums2[j - 1] > nums1[i]:
                # i 右移 （i偏小了，需要右移）
                left = i + 1
            elif i > left and nums1[i - 1] > nums2[j]:
                # i 左移 （i偏大了，需要左移）
                right = i - 1
            else:
                # i刚好合适，或i已达到数组边界
                if i == 0:
                    # 特殊情况处理1 nums1所有值 大于 nums2
                    maxLeft = nums2[j - 1]
                elif j == 0:
                    # 特殊情况处理2 nums1所有值 小于 nums2
                    maxLeft = nums1[i - 1]
                else:
                    # 正常情况
                    maxLeft = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    # 如果大数组的长度是奇数，中位数就是左半部分的最大值
                    return maxLeft

                if i == m:
                    # 因为nums1全部都在左侧，因此右侧最小值为nums2[j]
                    maxRight = nums2[j]
                elif j == n:
                    # 因为nums2全部都在左侧，因此右侧最小值为nums1[i]
                    maxRight = nums1[i]
                else:
                    maxRight = min(nums1[i], nums2[j])
                # 如果大数组的长度是偶数，取左侧最大值和右侧最小值的平均
                return (maxLeft + maxRight) / 2

        return 0.0


a = Solution()
list1 = [1, 3]
list2 = [2]
# print(a.findMedianSortedArrays2(list2, list1))

print(a.findMedianSortedArrays2(list1, list2))
