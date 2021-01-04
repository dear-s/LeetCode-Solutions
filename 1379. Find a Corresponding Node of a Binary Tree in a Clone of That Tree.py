
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        self.dfs(cloned, target)
        return self.ans
        
    def dfs(self, root, target):
        
        if root is None:
            return
        
        if root.val == target.val:
            self.ans = root
            return
        else:
            self.dfs(root.left, target)
            self.dfs(root.right, target)
        
