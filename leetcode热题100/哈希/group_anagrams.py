# 49. 字母异位词分组
# https://leetcode.cn/problems/group-anagrams/?envType=study-plan-v2&envId=top-100-liked
# 题解 https://leetcode.cn/problems/group-anagrams/solutions/2362226/li-yong-ha-xi-biao-jie-jue-zi-mu-yi-wei-jjiwo/?envType=study-plan-v2&envId=top-100-liked
from itertools import permutations


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # 最笨的办法，根据单词生成所有的异位词，然后逐个比对，是否有相应的异位词已被生成
        # 1 生成异位词字典
        AnagramsDict = {}

        # 2 遍历字符串数组
        for word in strs:
            # 2.1 生成所有的异位词
            # anagrams = [''.join(item) for item in permutations(word)]
            anagrams = {}
            for item in permutations(word):
                item = ''.join(item)
                anagrams[item] = item
            # print(anagrams)

            # 2.2 查找
            flag = 0
            for i in anagrams:
                if i in AnagramsDict:
                    # 2.3 有对应的异位词，添加进去
                    AnagramsDict[i].append(word)
                    print(word)
                    flag = 1
                    break

            # 2.4 没有对应的异位词，重新创建
            if flag == 0:
                AnagramsDict[word] = [word]

        return [item for index, item in AnagramsDict.items()]

    def groupAnagrams2(self, strs: list[str]) -> list[list[str]]:
        # 对于所有的异位词，可以有一个相同的异位词，排序好的，作为统一的键值
        # 1 生成异位词字典
        AnagramsDict = {}

        # 2 遍历字符串数组
        for word in strs:
            # 2.1 生成唯一的异位词标识
            # 对于所有的异位词，可以创建一个相同的共同使用的键值
            # anagrams = [''.join(item) for item in permutations(word)]
            identifier = ''.join(sorted(word))

            # 2.2 查找

            if identifier in AnagramsDict:
                # 2.3 有对应的异位词，添加进去
                AnagramsDict[identifier].append(word)
                print(word)

            # 2.3 没有对应的异位词，重新创建
            else:
                AnagramsDict[identifier] = [word]

        return [item for index, item in AnagramsDict.items()]

    def groupAnagrams3(self, strs: list[str]) -> list[list[str]]:
        # 1 生成异位词字典
        AnagramsDict = {}

        # 2 遍历字符串数组
        for word in strs:
            # 2.1 生成唯一的异位词标识
            # 对于所有的异位词，可以创建一个相同的共同使用的键值
            # anagrams = [''.join(item) for item in permutations(word)]
            identifier = ''.join(sorted(word))

            # 2.2 查找

            if identifier in AnagramsDict:
                # 2.3 有对应的异位词，添加进去
                AnagramsDict[identifier].append(word)
                print(word)

            # 2.3 没有对应的异位词，重新创建
            else:
                AnagramsDict[identifier] = [word]

        return list(AnagramsDict.values())


strs1 = ["hhhhu", "tttti", "tttit", "hhhuh", "hhuhh", "tittt"]

a = Solution()
print(a.groupAnagrams2(strs1))

# print(a.groupAnagrams())


# def generate_anagrams(word):
#     # 使用permutations生成所有可能的字母排列
#     anagrams = [''.join(perm) for perm in permutations(word)]
#     for i in permutations(word):
#         print(i)
#     return anagrams
#
#
# # 输入单词
# input_word = input("请输入一个单词: ")
#
# # 生成字母异位词
# result = generate_anagrams(input_word)
#
# # 打印结果
# print(f"{input_word}的所有字母异位词: {result}")
