
def fourSum(self, nums, target):
    def findNsum(l, r, target, N, result, results):
        if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:  # early termination
            return
        if N == 2: # two pointers solve sorted 2-sum problem
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        else: # recursively reduce N
            for i in range(l, r+1):
                if i == l or (i > l and nums[i-1] != nums[i]):
                    findNsum(i+1, r, target-nums[i], N-1, result+[nums[i]], results)

    nums.sort()
    results = []
    findNsum(0, len(nums)-1, target, 4, [], results)
    return results
# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         m = {}
#         result = []
#         nums.sort()
#         if len(nums) < 4 or target < nums[0]*4 or target > nums[-1]*4:
#             return result
#         for i in range(0, len(nums)-3):
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             current_target = target - nums[i]
#             if current_target < nums[i+1]*3 or current_target > nums[-1]*3:
#                 continue
#             for j in range(i+1, len(nums)-2):
#                 current_target = target - nums[i] - nums[j]
#                 if current_target < nums[j+1]*2 or current_target > nums[-1]*2:
#                     continue
#                 if j > i+1 and nums[j] == nums[j-1]:
#                     continue
#                 l = j+1
#                 r = len(nums)-1
#                 while l < r:
#                     current = nums[i] + nums[j]+ nums[l] + nums[r]
#                     if current == target:
#                         result.append([nums[i], nums[j], nums[l], nums[r]])
#                         while l < r and nums[l] == nums[l+1]:
#                             l += 1
#                         while l < r and nums[r] == nums[r-1]:
#                             r -= 1
#                         l+=1
#                         r -= 1
#                     elif current < target:
#                         l += 1
#                     else:
#                         r -= 1
#         return result            