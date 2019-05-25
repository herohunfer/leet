class Solution {
public:
    TreeNode* bstToGst(TreeNode* root) {
        int acc = 0;
        dfs(root, acc);
        return root;
    }
    
    void dfs(TreeNode * node, int & acc) {
        if (node != nullptr) {
            dfs(node->right, acc);
            int temp = node->val;
            node->val += acc;
            acc += temp;
            dfs(node->left, acc);
        }
    }
};

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def bstToGst(self, root: TreeNode) -> TreeNode:
#         self.helper(root, 0)
#         return root
    
#     def helper(self, root: TreeNode, rightTotal: int) -> int:
#         if not root:
#             return 0
#         rightVal = self.helper(root.right, rightTotal)
#         root.val += rightVal + rightTotal
#         leftVal = self.helper(root.left, root.val)
#         return leftVal + (root.val-rightTotal)