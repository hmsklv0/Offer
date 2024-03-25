class Solution:
    def minNumber(self, nums: list[int]) -> str:
        # 很麻烦
        h = ''
        def smaller(a: str, b: str) -> bool:
            nonlocal h
            ai, bi = len(a), len(b)
            if a[0] < b[0]:
                return True
            elif a[0] > b[0]:
                return False
            elif ai == 1 and bi == 1:
                return True
            else:
                # a[0] = b[0] and ai != bi
                if ai > bi == 1:
                    if ai == 2:
                        return smaller(a[1:], h)
                    return smaller(a[1:], b)
                elif ai < bi and ai == 1:
                    if bi == 2:
                        return smaller(h, b[1:])
                    return smaller(a, b[1:])
                else:

                    return smaller(a[1:], b[1:])

        nums_str = [str(i) for i in nums]
        for i in range(len(nums_str)):
            for j in range(len(nums_str) - 1, i, -1):
                h = nums_str[i][0]
                if not smaller(nums_str[i], nums_str[j]):
                    # 调换位置

                    nums_str[i], nums_str[j] = nums_str[j], nums_str[i]

        return ''.join(nums_str)


    def minNumber2(self, nums: list[int]) -> str:

        def smaller(a: str, b: str) -> bool:
            ab, ba = a + b, b + a
            if ab < ba:
                return True
            if ab > ba:
                return False

        nums_str = [str(i) for i in nums]
        for i in range(len(nums_str)):
            for j in range(len(nums_str) - 1, i, -1):
                h = nums_str[i][0]
                if not smaller(nums_str[i], nums_str[j]):
                    # 调换位置

                    nums_str[i], nums_str[j] = nums_str[j], nums_str[i]

        return ''.join(nums_str)


test_list = [3, 30, 34, 5, 9]
test_list = [824,938,1399,5607,6973,5703,9609,4398,8247]
# test_list = [10, 2]
solution = Solution()
print(solution.minNumber2(test_list))


def smaller(a: str, b: str) -> bool:
    ai, bi = len(a), len(b)
    if a[0] < b[0]:
        return True
    elif a[0] > b[0]:
        return False
    elif ai == 1 and bi == 1:
        return True
    else:
        # a[0] = b[0] and ai != bi
        # 3 39
        # 8247 824
        if ai > bi == 1:
            return smaller(a[1:], b)
        elif ai < bi and ai == 1:
            return smaller(a, b[1:])
        else:
            return smaller(a[1:], b[1:])
print(smaller("824", "8247"))


1399439856075703697382482479389609
1399439856075703697382478249389609