"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        # root, left, right
        self.ans = []
        
        def res(root):
            if root is None:
                return
            self.ans.append(root.val)
            
            # multiple children
            for child in root.children:
                res(child)
                
        res(root)  
        return self.ans
        
