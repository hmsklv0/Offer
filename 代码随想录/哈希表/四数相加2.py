from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        map1 = {}
        for i in nums1:
            for j in nums2:
                cur_num = map1.setdefault(i + j, 0) + 1
                map1[i + j] = cur_num
        count = 0
        for i in nums3:
            for j in nums4:
                if - (i + j) in map1:
                    count += map1[-i - j]
        return count
