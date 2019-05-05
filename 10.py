# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# better solution

# https://leetcode.com/problems/regular-expression-matching/discuss/5723/My-DP-approach-in-Python-with-comments-and-unittest
# Here are some conditions to figure out, then the logic can be very straightforward.

# 1, If p.charAt(j) == s.charAt(i) :  dp[i][j] = dp[i-1][j-1];
# 2, If p.charAt(j) == '.' : dp[i][j] = dp[i-1][j-1];
# 3, If p.charAt(j) == '*': 
#    here are two sub conditions:
#                1   if p.charAt(j-1) != s.charAt(i) : dp[i][j] = dp[i][j-2]  //in this case, a* only counts as empty
#                2   if p.charAt(i-1) == s.charAt(i) or p.charAt(i-1) == '.':
#                               dp[i][j] = dp[i-1][j]    //in this case, a* counts as multiple a 
#                            or dp[i][j] = dp[i][j-1]   // in this case, a* counts as single a
#                            or dp[i][j] = dp[i][j-2]   // in this case, a* counts as empty
#     in summary:
#         dp[i][j] = dp[i][j-2]
#                     or dp[i-1][j] if p[i-1] == s[i] or p[i-1] = '.'
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p)+1) for _ in range(len(s)+1)]
        dp[0][0] = True
        for j in range(len(p)):
            if p[j] == "*" and dp[0][j-1]:
                dp[0][j+1] = True
            
        for i in range(0, len(s)):
            for j in range(0, len(p)):
                if p[j] != "*":
                    dp[i+1][j+1] = dp[i][j] and (s[i] == p[j] or p[j] == '.')
                else:
                    dp[i+1][j+1] = dp[i+1][j-1] or dp[i+1][j]
                    
                    if p[j-1] == s[i] or p[j-1] == '.':
                        dp[i+1][j+1] |= dp[i][j+1]
        
        return dp[-1][-1]

# Old solution
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         # print("s={} p={}".format(s, p))
#         i = 0
#         j = 0
#         while j < len(p):
#             if p[j] == '.':
#                 if j < len(p)-1 and p[j+1] == '*':
#                     # try match
#                     for k in range(i, len(s)+1):
#                         if self.isMatch(s[k:], p[j+2:]):
#                             return True
#                     return False
#             elif ord(p[j]) >= ord('a') and ord(p[j]) <= ord('z'):
#                 if j < len(p)-1 and p[j+1] == '*':
#                     # try match multiple p[i]
#                     for k in range(i, len(s)+1):
#                         if self.isMatch(s[k:], p[j+2:]):
#                             return True
#                         if k < len(s) and s[k] != p[j]:
#                             break
#                     return False
#                 else:
#                     if i < len(s) and s[i] != p[j]:
#                         return False
#             i += 1
#             j += 1
#         if i != len(s):
#             return False
#         else:
#             return True