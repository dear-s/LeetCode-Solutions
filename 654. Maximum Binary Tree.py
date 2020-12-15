
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        
        
        # binary tree
        # root - maximum number
        # left, right - order taken care of
        
        if len(nums) == 0:
            return None
        
        root_value = max(nums)
        index_of_root = nums.index(root_value)
        
        left_array = nums[:index_of_root]
        right_array = nums[index_of_root+1:]
        
        root = TreeNode(root_value)
        root.left = self.constructMaximumBinaryTree(left_array)
        root.right = self.constructMaximumBinaryTree(right_array)
        
        return root
        
