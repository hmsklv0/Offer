class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_dict = {}
        # 读取
        for i in ransomNote:
            cur_num = ransomNote_dict.setdefault(i, 0) + 1
            ransomNote_dict[i] = cur_num

        for j in magazine:
            if j in ransomNote_dict:
                ransomNote_dict[j] -= 1

        for k, v in ransomNote_dict.items():
            if v > 0:
                return False
        return True

    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        # 利用数组 map
        ransomNote_dict = [0 for _ in range(26)]

        # 读取
        for i in ransomNote:
            ransomNote_dict[ord(i) - ord('a')] += 1

        for j in magazine:
            char_index = ord(j) - ord('a')
            if ransomNote_dict[char_index] == 0:
                continue
            else:
                ransomNote_dict[char_index] -= 1

        for v in ransomNote_dict:
            if v > 0:
                return False
        return True
