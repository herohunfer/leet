#Runtime: 38 ms
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lowest = sys.maxsize
        lower = sys.maxsize
        for num in nums:
            if num <= lowest:
                lowest = num
            elif num <= lower:
                lower = num
            else:
                return True
        return False
