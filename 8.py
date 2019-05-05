class Solution:
    def myAtoi(self, str: str) -> int:
        L = str.strip().split()
        if len(L) ==  0:
            return 0
        s = L[0]
        start = 0
        sign = False
        if s[0] == '+':
            start = 1
        elif s[0] == '-':
            sign = True
            start = 1
        elif s[0] not in '0123456789':
            return 0
        val = 0
        for i in range(start, len(s)):
            if s[i] not in '0123456789':
                break
            val = 10*val + ord(s[i]) - ord('0')
        
        if sign:
            if -val < -2**31:
                return -2**31
            return -val
        else:
            if val > 2**31-1:
                return 2**31-1
            return val