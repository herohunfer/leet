# amazing to see using set like this.
def lastStoneWeightII(self, A):
    dp = {0}
    sumA = sum(A)
    for a in A:
        dp |= {a + i for i in dp}
    return min(abs(sumA - i - i) for i in dp)

# https://leetcode.com/problems/last-stone-weight-ii/discuss/294973/Python-1-line
def lastStoneWeightII(self, A):
        return min(reduce(lambda dp, y: {x + y for x in dp} | {abs(x - y) for x in dp}, A, {0}))
# class Solution:
#     def lastStoneWeightII(self, stones: List[int]) -> int:
#         smallest = 3000
#         path = set()
#         path.add(stones[0])
#         path.add(-stones[0])
#         for stone in stones[1:]:
#             new_path = set()
#             for item in path:
#                 val1 = item + stone
#                 new_path.add(val1)
#                 val2 = item-stone
#                 new_path.add(val2)
#             path = new_path
#         for val in path:
#             if abs(val) < smallest:
#                 smallest = abs(val)
#         return smallest
