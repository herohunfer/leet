# Runtime: 525 ms
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        s = [root]
        pos = 0
        res = 1
        start = 0
        end = 1
        while pos < len(s):
            if s[pos] is not None:
                if len(s) > end:
                    s.append(s[pos].left)
                    s.append(s[pos].right)
                elif s[pos].left is not None:
                    s.append(s[pos].left)
                    s.append(s[pos].right)
                elif s[pos].right is not None:
                    s.append(s[pos].right)        
            elif len(s) > end:
                s.append(None)
                s.append(None)
            pos += 1
            if pos == end:
                current = pos
                start = end
                while current < len(s):
                    if s[current] is not None:
                        res = max(current+1-start, res)
                        end = current+1
                    current += 1
                del s[end:]
        return res
