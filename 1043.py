class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        m = [[0]*len(A) for _ in range(K)]
        for i in range(K):
            for j in range(len(A)):
                if i == 0:
                    m[i][j] = A[j]
                elif j == 0:
                    m[i][j] = A[j]
                else:
                    m[i][j] = m[i-1][j-1] if m[i-1][j-1] > A[j] else A[j]
        res = [0] * (len(A)+1)
        for i in range(len(A)):
            for j in range(K):
                if i-j >= 0 and m[j][i]*(j+1) + res[i-j-1+1] > res[i+1]:
                    res[i+1] = m[j][i]*(j+1) + res[i-j] 
        return res[-1]
                
