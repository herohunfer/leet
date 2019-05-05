# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
# Return the sum of the three integers. 
# You may assume that each input would have exactly one solution.
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return target
                result = s if abs(target-s) < abs(target-result) else result
                if s < target: 
                    l += 1
                else:
                    r -= 1
        return result