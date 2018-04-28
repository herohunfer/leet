#Runtime: 169 ms
# Not optimal. can use set to store data
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getSum(self, root):
        if root is None:
            return 0
        return self.getSum(root.left)+self.getSum(root.right)+root.val
    def checkTree(self, root, sum):
        if root is None:
            return False, 0
        checkLeft, sumLeft = self.checkTree(root.left, sum)
        checkRight, sumRight = self.checkTree(root.right, sum)
        total = sumLeft + sumRight + root.val
        return checkLeft or checkRight or total*2 == sum, total
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None or (root.left is None and root.right is None):
            return False
        totalSum = self.getSum(root)
        return self.checkTree(root, totalSum)[0]
        
