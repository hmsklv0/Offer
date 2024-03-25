class Solution:
    def mySqrt(self, x: int) -> int:
        # 思路，right - 1
        # [left, right) 左闭右开区间
        # 寻找当中的mid满足条件，其余与二叉搜索一致
        left, right = 0, x + 1

        while left < right:
            mid = (left + right) // 2
            if mid * mid <= x < pow(mid + 1, 2):
                return mid
            elif mid * mid > x:
                right = mid
            else:
                left = mid + 1

        return right - 1
