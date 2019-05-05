# Given a string, find the length of the longest substring without repeating characters.
# Input: "abcabcbb"
# Output: 3 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        current = 0
        longest = 0
        for index, val in enumerate(s):
            if val in m and index - m[val] <= current:
                current = index - m[val] -1
            m[val] = index
            current += 1
            if current > longest:
                    longest = current
        return longest