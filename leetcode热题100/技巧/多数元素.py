# 投票算法

import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        vote = nums[0]
        for i in range(len(nums)):
            # 这里需要区别一下，放在最前，count = 0
            if count == 0:
                vote = nums[i]
                count = 0


            if nums[i] != vote:
                count -= 1
            else:
                count += 1

        return vote

    def majorityElement2(self, nums: List[int]) -> int:
        count = 0
        vote = nums[0]
        for i in range(len(nums)):

            if nums[i] != vote:
                count -= 1
            else:
                count += 1
            # 放在后面，需要count = 1，避免为负数，不再进行更新
            if count == 0:
                vote = nums[i]
                count = 1
        return vote

    def majorityElement3(self, nums: List[int]) -> int:
        a = collections.Counter(nums)
        return a.most_common()[0][0]
