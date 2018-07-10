class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        depth, node = self.subtreeWithDeepest(root)
        return node
    
    def subtreeWithDeepest(self, root):
        if root is None:
            return 0, None
        leftDepth, leftNode = self.subtreeWithDeepest(root.left)
        rightDepth, rightNode = self.subtreeWithDeepest(root.right)
        if leftDepth == rightDepth:
            return (leftDepth+1, root)
        else:
            return (leftDepth+1, leftNode) if leftDepth > rightDepth else (rightDepth+1, rightNode)
