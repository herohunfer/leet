# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]