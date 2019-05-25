# Given a 32-bit signed integer, reverse digits of an integer.


class Solution:
    def reverse(self, x: int) -> int:
        sign = x < 0
        if sign:
            x = -x
        y = 0
        while x> 0:
            y = 10*y + x%10
            x //= 10
        if sign:
            if -y < -2**31-1:
                return 0
            return -y
        else:
            if y > 2**31:
            
                return 0
            return y