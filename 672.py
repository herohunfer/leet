class Solution(object):
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if m == 0:
            return 1
        if n == 1: 
            return 2
        if n == 2:
            return 3 if m == 1 else 4
        if n >= 3:
            if m == 1:
                return 4
            else:
                return 7 if m ==2 else 8
