
		
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        self.leafSequence1_arr = []
        self.leafSequence2_arr = []
        
        self.leafSequence1(root1)
        self.leafSequence2(root2)
        
        print("self.leafSequence1_arr: ", self.leafSequence1_arr)
        print("self.leafSequence2_arr: ", self.leafSequence2_arr)
        
        if self.leafSequence1_arr == self.leafSequence2_arr:
            return True
        else:
            return False
        
    def leafSequence1(self, root):
        if root is None:
            return
        
        if root.left is None and root.right is None:
            self.leafSequence1_arr.append(root.val)
        
        self.leafSequence1(root.left)
        self.leafSequence1(root.right)
        
    def leafSequence2(self, root):
        if root is None:
            return
        
        if root.left is None and root.right is None:
            self.leafSequence2_arr.append(root.val)
        
        self.leafSequence2(root.left)
        self.leafSequence2(root.right)
        
		
		
