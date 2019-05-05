
# Solution 2

# Here I wrote an actual Python generator. I allow myself to put the yield q at the end of the line 
# because it's not that bad and because in "real life" I use Python 3 where I just say yield from generate(...).
def generateParenthesis(self, n):
    def generate(p, left, right):
        if right >= left >= 0:
            if not right:
                yield p
            for q in generate(p + '(', left-1, right): yield q
            for q in generate(p + ')', left, right-1): yield q
    return list(generate('', n, n))
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         result = [""]
#         count = [0]
#         remain = [n]
#         for _ in range(2*n):
#             temp = []
#             new_count = []
#             new_remain = []
#             for i,s in enumerate(result):
#                 if count[i] > 0:
#                     temp.append(s+")")
#                     new_count.append(count[i]-1)
#                     new_remain.append(remain[i])
#                 if remain[i] > 0:
#                     temp.append(s+"(")
#                     new_count.append(count[i]+1)
#                     new_remain.append(remain[i]-1)
#             result = temp
#             count = new_count
#             remain = new_remain
#         return result



# Solution 3

# Improved version of this. Parameter open tells the number of "already opened" parentheses, and I continue the recursion as long as I still have to open parentheses (n > 0) and I haven't made a mistake yet (open >= 0).

# def generateParenthesis(self, n, open=0):
#     if n > 0 <= open:
#         return ['(' + p for p in self.generateParenthesis(n-1, open+1)] + \
#                [')' + p for p in self.generateParenthesis(n, open-1)]
#     return [')' * open] * (not n)