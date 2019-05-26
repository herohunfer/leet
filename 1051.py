class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        hsort = sorted(heights)
        return sum([1 if heights[i] != hsort[i] else 0 for i in range(len(heights))])
