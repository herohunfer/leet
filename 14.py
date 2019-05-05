# this is a cool solution. https://leetcode.com/problems/longest-common-prefix/discuss/6911/Simple-Python-solution
# zip(*strs) will return letter group in each position, and only return number of groups equal to minimum length.
# set(letter_group) to check if there are more than one unique letters in group
# >>> strs = ["abcd", "abc", "abce"]
# >>> list(zip(*strs))
# [('a', 'a', 'a'), ('b', 'b', 'b'), ('c', 'c', 'c')]

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
            
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)
# class Solution:
#     def longestCommonPrefix(self, m):
#         if not m: return ''
# 				#since list of string will be sorted and retrieved min max by alphebetic order
#         s1 = min(m)
#         s2 = max(m)

#         for i, c in enumerate(s1):
#             if c != s2[i]:
#                 return s1[:i] #stop until hit the split index
#         return s1
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if len(strs) == 0:
#             return ""
#         if any(len(x) == 0 for x in strs):
#             return ""
#         for i in range(len(strs[0])):
#             c = strs[0][i]
#             for j in range(len(strs)):
#                 if i >= len(strs[j]) or strs[j][i] != c: 
#                     return strs[0][:i]
#         return strs[0]