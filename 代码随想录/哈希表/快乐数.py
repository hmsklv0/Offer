class Solution:
    def isHappy(self, n: int) -> bool:
        def get_sum(cur_num: int) -> int:
            cur_res = 0
            while cur_num > 0:
                cur_res += pow(cur_num % 10, 2)
                cur_num = cur_num // 10
            print(cur_res)
            return cur_res

        set1 = set()
        while True:
            res = get_sum(n)
            if res == 1:
                return True
            if res in set1:
                return False
            set1.add(res)
            n = res

a = Solution()
a.isHappy(19)