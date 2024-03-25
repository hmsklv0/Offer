class Solution:
    def isStraight(self, nums: list[int]) -> bool:
        repeat = set()
        ma, mi = 0, 14
        for i in nums:
            if i == 0:
                continue
            ma = max(ma, i)
            mi = min(mi, i)

            if i in repeat:
                return False
            repeat.add(i)

        return ma - mi < 5

