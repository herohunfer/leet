# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = {}
        longest = 0
        low = 0
        for i in range(len(s)):
            # check remaining length
            if len(s)-i <= longest//2:
                break
            left = i-1
            right = i+1
            while right < len(s) and s[right] == s[i]:
                right+=1
            # skip duplicates
            i = right
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left-=1
                right+=1
            if (right-1) - (left+1) + 1 > longest:
                low = left+1
                longest = right-1 - (left+1) + 1
        return s[low: low+longest]