from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set(nums1)
        res2 = set(nums2)
        return list(res.intersection(res2))


    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res1 = set(nums1)
        res = set()
        for i in nums2:
            if i in res1:
                res.add(i)
        return list(res)
