class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 举例
        # 初始 i
        # 翻转 n - i
        # 二次翻转 k- (n-i)= k + i - n(以 0,k 区间中轴翻转)
        # 二次翻转 k + i(以 k,n 区间中轴翻转)
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums: list[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


a = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
a.rotate(nums, k)
print(nums)