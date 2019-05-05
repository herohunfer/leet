# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# You may assume nums1 and nums2 cannot be both empty.

# Example 1:

# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        N1 = len(nums1)
        N2 = len(nums2)
        if N1 > N2:
            return self.findMedianSortedArrays(nums2, nums1)
        k = (N1+N2+1)//2
        l = 0
        r = N1
        
        while l < r:
            m1 = l + (r-l)//2
            m2 =  k-m1
            if nums1[m1] < nums2[m2-1]:
                l = m1+1
            else:
                r = m1
        
        m1 = l
        m2 = k-l
        
        c1 = -sys.maxsize-1
        c2 = sys.maxsize
        
        if m1 <= 0:
            c1 = nums2[m2-1]
        elif m2 <= 0:
            c1 = nums1[m1-1]
        else:
            c1 = max(nums1[m1-1], nums2[m2-1])
        if (N1+N2) % 2 == 1:
            return c1
        
        if m1 >= N1:
            c2 = nums2[m2]
        elif m2 >= N2:
            c2 = nums1[m1]
        else:
            c2 = min(nums1[m1], nums2[m2])
        return (c1+c2)/2    
            
            
