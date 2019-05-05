class Solution:
    def numSpecialEquivGroups(self, A):
        return len(set("".join(sorted(s[0::2])) + "".join(sorted(s[1::2])) for s in A))
# class Solution:
#     def numSpecialEquivGroups(self, A: List[str]) -> int:
#         m = set()
#         res = 0
#         for i in A:
#             g1 = i[::2]
#             g2 = i[1::2]
#             g1 = ''.join(sorted(g1))
#             g2 = ''.join(sorted(g2))
#             if g1 + g2 not in m:
#                 m.add(g1+g2)
#                 res +=1
#         return res