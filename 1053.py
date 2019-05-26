class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        for i in range(len(A)-2, -1, -1):
            if A[i] > A[i+1]:
                for j in range(len(A)-1, i, -1):
                    while j  > i and A[j] == A[j-1]:
                        j -= 1
                    if A[i]> A[j]:
                        A[i], A[j] = A[j], A[i]
                        return A
        return A
