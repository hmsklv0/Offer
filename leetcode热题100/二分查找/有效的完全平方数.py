class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # 与X的平方根相同的思路，找到结束的判断条件，其余的与二分搜索无异
        left, right = 0, num + 1
        while left < right:
            mid = (left + right) // 2
            if pow(mid, 2) == num:
                return True
            elif pow(mid, 2) < num:
                left = mid + 1
            else:
                # pow(mid, 2) > num
                right = mid
        return False
