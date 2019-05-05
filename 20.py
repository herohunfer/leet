class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for i in s:
            if i == ")" or i == "}" or i == "]":
                if len(stack) == 0 or stack[-1] != m[i]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)
        if len(stack) > 0:
            return False
        else:
            return True

# class Solution(object):
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         n = len(s)
#         if n == 0:
#             return True
        
#         if n % 2 != 0:
#             return False
            
#         while '()' in s or '{}' in s or '[]' in s:
#             s = s.replace('{}','').replace('()','').replace('[]','')
        
#         if s == '':
#             return True
#         else:
#             return False