from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 双指针
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:
                # 左边为 递增序列
                if nums[left] <= target < nums[mid]:
                    # 如果 target 在左边的递增序列
                    res = self.binary_search(nums[left:mid], target)

                    return res if res == -1 else left + res
                else:
                    # 如果 target 在右边的非递增序列
                    left = mid + 1
            else:
                # if nums[mid] < nums[left]
                # 右边为 递增序列
                if nums[mid] < target <= nums[right]:
                    # 如果 target 在右边的递增序列
                    res = self.binary_search(nums[mid: right + 1], target)
                    return res if res == -1 else mid + res
                else:
                    # 如果 target 在左边的非递增序列
                    right = mid - 1
        return -1

    def binary_search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


a = Solution()
list1 = [4, 5, 6, 7, 0, 1, 2]
list2 = [1]
print(a.search(list1, 0))
