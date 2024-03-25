class Solution:
    def translateNum(self, num: int) -> int:

        def helper(slice_num: str) ->int:
            if int(slice_num) >= 26 or int(slice_num) <= 9:
                # 不可拆，变化为 1
                return 1
            elif int(slice_num) < 26:
                # 可拆，变化为 2
                return 2

        str_num = str(num)
        int_num_len = len(str_num)
        if int_num_len == 0:
            return 0
        elif int_num_len == 1:
            return 1
        f0 = 1
        f1 = helper(str_num[:2])
        for i in range(2, int_num_len):
            if helper(str_num[i-1:i+1]) == 2:
                # 若为2，则最后两位可拆分，转移方程写为
                f1, f0 = f1 + f0, f1
            else:
                f1, f0 = f1, f1
            pass
        return f1

solution = Solution()
test = 506
print(solution.translateNum(test))