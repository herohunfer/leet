class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        for i in range(0, len(A)-1, -1):
            if A[i] > A[i+1]:
                for j in range(0, len(A), -1):
                    if A[i]> A[j]:
                        temp = A[pos]
                        A[pos] = A[i]
                        A[i] = temp
                        return A
        return A
