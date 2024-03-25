class Solution:
    def minArray(self, numbers: list[int]) -> int:
        # 旋转数组的最小数字，这种方法不好，无法判断整个数组旋转过来的情况
        head = numbers[0]
        length = len(numbers)
        i = 1
        while i <= length:
            if numbers[-i] >= head:
                return numbers[-i + 1]
            i += 1

    def minArray2(self, numbers: list[int]) -> int:
        # 旋转数组的最小数字，可行，笨办法，数大小
        head = numbers[0]
        length = len(numbers)
        i = 0
        while i <= length - 2:
            if numbers[i] > numbers[i + 1]:
                return numbers[i + 1]
            i += 1
        return head

    def minArray3(self, numbers: list[int]) -> int:
        # 将数组分为两部分，左数组 || 右数组
        # 求旋转点
        i, j = 0, len(numbers) - 1
        while i < j:
            m = (i + j) // 2
            if numbers[m] < numbers[j]:
                # 判断 m 在哪儿，是左序数组还是右序数组
                # 若小于，则 m 在右，旋转点在 [i, m]
                j = m
            elif numbers[m] > numbers[j]:
                # 若大于，则 m 在左,旋转点在 [m + 1, j]
                i = m + 1
            else:
                # numbers[m] == numbers[j]:
                # 无法判断，旋转点在哪儿
                # 如 10111， 11101
                # j = j - 1, 逐步缩小空间
                return min(numbers[i:j])
        return numbers[i]


solution = Solution()
numbers = [2, 2, 2, 0, 1]
print(solution.minArray3(numbers))
