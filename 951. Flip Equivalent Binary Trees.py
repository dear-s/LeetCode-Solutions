
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        
        # dfs approach - https://www.youtube.com/watch?v=v2tOLEE4A9E
        return self.dfs(root1, root2)
    
    
    def dfs(self, one, two):
        if one is None and two is None:
            return True

        elif one is None or two is None:
            return False

        elif one.val != two.val:
            return False

        # 1. not flipped        2. flipped [2 options to consider]
        not_flip = self.dfs(one.left, two.left) and self.dfs(one.right, two.right)
        flipped = self.dfs(one.right, two.left) and self.dfs(one.left, two.right)

        return not_flip or flipped
        
    
