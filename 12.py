# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
class Solution(object):
    def intToRoman(self, num):
        dict = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = ""
        for letter, n in zip(dict, nums):
            result += letter * (num // n)
            num %= n
        return result
# class Solution:
#     def intToRoman(self, num: int) -> str:
#         s = ""
#         M, num = num//1000, num%1000
#         s += "M" * M
#         C, num = num//100, num%100
#         if C==9:
#             s+= "CM"
#         elif C==4:
#             s+= "CD"
#         else:
#             s+= "D"*(C//5)+ "C"*(C%5)
        
#         X, num = num//10, num%10
#         if X==9:
#             s+= "XC"
#         elif X==4:
#             s+= "XL"
#         else:
#             s+= "L"*(X//5)+"X"*(X%5)
        
#         I = num
#         if I==9:
#             s+="IX"
#         elif I==4:
#             s+="IV"
#         else:
#             s+= "V"*(I//5)+"I"*(I%5)
#         return s    