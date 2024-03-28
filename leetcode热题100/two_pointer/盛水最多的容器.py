# 题目 https://leetcode.cn/problems/container-with-most-water/?envType=study-plan-v2&envId=top-100-liked
# 题解 https://leetcode.cn/problems/container-with-most-water/solutions/11491/container-with-most-water-shuang-zhi-zhen-fa-yi-do/?envType=study-plan-v2&envId=top-100-liked
# 11. 盛最多水的容器

class Solution:
    def maxArea(self, height: list[int]) -> int:
        # 传统思路
        max_volume = 0
        for i in range(len(height)):
            j = i + 1
            while j < len(height):
                max_volume = max(max_volume, (j - i) * min(height[j], height[i]))
                j += 1
        return max_volume

    def maxArea2(self, height: list[int]) -> int:
        # 双指针
        i, j, max_volume = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                max_volume = max(max_volume, (j - i) * height[i])
                # 短边前进
                i += 1
            else:
                max_volume = max(max_volume, (j - i) * height[j])
                # 短边前进
                j -= 1
        return max_volume

    def maxArea3(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        ans = 0
        while left < right:
            if height[left] < height[right]:
                ans = max(ans, height[left] * (right - left))
                left += 1
            else:
                ans = max(ans, height[right] * (right - left))
                right -= 1
        return ans


a = Solution()
print(a.maxArea2([1, 8, 6, 2, 5, 4, 8, 3, 7]))
