# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, val in enumerate(nums):
            if target - val in d:
                return d[target-val], index
            d[val] = index