# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

class Solution:
# @param {string} s
# @return {integer}
def romanToInt(self, s):
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    z = 0
    for i in range(0, len(s) - 1):
        if roman[s[i]] < roman[s[i+1]]:
            z -= roman[s[i]]
        else:
            z += roman[s[i]]
    return z + roman[s[-1]]

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         dict = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
#         nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#         current = 0
#         index = 0
#         result = 0
#         while current < len(dict):
#             if s[index: index + len(dict[current])] == dict[current]:
#                 result += nums[current]
#                 index += len(dict[current])
#             else:
#                 current += 1
#         return result