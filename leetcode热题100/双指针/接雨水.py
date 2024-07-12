# trapping-rain-water
# 接雨水
from typing import List


class Solution:
    def trap(self, height: list[int]) -> int:
        left_pointer, right_pointer = 0, 0

        result = 0
        height_len = len(height)
        if height_len == 1:
            return 0
        # 1 寻找谷峰
        local_maxima_indices = []
        # 寻找第一个峰
        for i in range(height_len - 1):
            if height[i] > height[i + 1]:
                local_maxima_indices.append((i, height[i]))
                print("第一个峰", local_maxima_indices[0])
                break
            elif height[i] < height[i + 1]:
                break
        for i in range(1, height_len - 1):
            if height[i - 1] < height[i] and height[i] >= height[i + 1]:
                local_maxima_indices.append((i, height[i]))
                print((i, height[i]))
        # 寻找最后一个峰
        for i in range(1, height_len):
            if height[-i] > height[-i - 1]:
                local_maxima_indices.append((len(height) - i, height[-i]))
                print("最后一个峰", (len(height) - i, height[-i]))
                break
            elif height[-i] < height[-i - 1]:
                break
        print("真实局部峰顶:\t", local_maxima_indices)
        # 2 去除虚假的峰顶
        right_pointer = 1
        while right_pointer < len(local_maxima_indices) - 1:
            # 虚假的峰顶
            if local_maxima_indices[right_pointer - 1][1] >= local_maxima_indices[right_pointer][1] and \
                    local_maxima_indices[right_pointer][1] <= local_maxima_indices[right_pointer + 1][1]:
                r = local_maxima_indices.pop(right_pointer)
                print("pop ", r)
                if right_pointer > 1:
                    right_pointer -= 1
                continue

            right_pointer += 1

        print("局部峰顶:\t\t", local_maxima_indices)

        # 3 生成标准线
        if len(local_maxima_indices) <= 1:
            return 0
        line = [0 for i in range(local_maxima_indices[0][0])]

        for i in range(1, len(local_maxima_indices)):
            line_data = min(local_maxima_indices[i][1], local_maxima_indices[i - 1][1])
            line.extend([line_data for i in range(local_maxima_indices[i][0] - local_maxima_indices[i - 1][0])])

        for i in range(local_maxima_indices[0][0], local_maxima_indices[-1][0]):
            result += max(line[i] - height[i], 0)
        print("雨水线:\t\t", line)
        print("原本线:\t\t", height)

        return result

    def trap2(self, height: List[int]) -> int:
        # 官方题解1
        # 找到每个 i 所对应的左右最大边
        left_max, right_max = [0 for _ in range(len(height))], [0 for _ in range(len(height))]

        left_max[0] = height[0]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[-1] = height[-1]
        # 修改为2
        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        ans = 0
        for j in range(len(height)):
            # 不用担心为负值，因为如果height[j]如果比两边都高，那么left_max[j] 和 right_max[j]都将为其本身
            ans += min(left_max[j], right_max[j]) - height[j]
        return ans

    def trap3(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height)-1
        left_max, right_max = 0, 0

        while left <= right:
            # https://leetcode.cn/problems/trapping-rain-water/?envType=study-plan-v2&envId=top-100-liked
            # 更新自己的左右最大边界
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            # 可行性分析，从两边往中间靠，核心原理
            # 当两边最高处比较，一定是较小的一端先靠过来，因此比较的就是较小的那边最大值去减当前height
            if height[left] < height[right]:
                ans += left_max - height[left]
                left += 1
            else:
                ans += right_max - height[right]
                right -= 1
        return ans


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height2 = [4, 2, 0, 3, 2, 5]  # 第一个峰和最后一个峰
height3 = [5, 5, 1, 7, 1, 1, 5, 2, 7, 6]  # 平缓的第一个峰
height4 = [6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2, 7, 5, 3, 0, 1, 2, 1, 3, 4, 6, 8, 1, 3]  # 高的峰中间夹着比较低的峰
height5 = [9, 6, 8, 8, 5, 6, 3]  # 平缓的峰
height6 = [8, 8, 1, 5, 6, 2, 5, 3, 3, 9]  # 高的峰中间夹着比较低的峰，删除较低的峰后，前面的峰变成地峰
height7 = [1, 1, 1, 1, 1, 1, 1, 1]  # 重复元素
a = Solution()
print(a.trap(height6))
