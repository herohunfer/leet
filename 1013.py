class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        if total % 3 != 0:
            return False
        part = total //3
        l = 0
        r = len(A)-1
        sumL = A[l]
        sumR = A[r]
        while l < r and sumL != part:
            l += 1
            sumL += A[l]
        while l < r and sumR != part:
            r -= 1
            sumR += A[r]
        return l < r    
