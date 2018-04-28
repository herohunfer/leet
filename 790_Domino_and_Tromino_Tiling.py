class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        T = [0] * 2000
        T[0] = 1
        T[1] = 0
        T[2] = 1
        T[3]=1
        T[4]=2
        for i in range(6, 2*N+1, 2):
            T[i] = T[i-2] + 2*T[i-3] + T[i-4]
            T[i-1] = T[i-3] + T[i-4]
        return (T[2*N])%(pow(10,9)+7)