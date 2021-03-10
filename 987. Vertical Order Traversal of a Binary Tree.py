
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        
        
        # start root at (0,0)
        # dfs traversal and give coords to nodes
        
        self.node_coord = {}
        self.node_coord[root.val] = [0,0]
        
        x = 0
        y = 0
        
        if root.left:
            self.dfs(root.left, x-1, y-1)
        if root.right:
            self.dfs(root.right, x+1, y-1)
                    
        
        # arrange according to x and then y
        min_x = float('inf')
        max_x = float('-inf')
        min_y = 0
        for k,v in self.node_coord.items():
            max_x = max(max_x, v[0])
            min_x = min(min_x, v[0])
            min_y = min(min_y, v[1])
            
        output = [[] for x in range(min_x, max_x+1)]
        
        # how much negative -- add that much to x_coord - [converting coords - positive]
        for k,v in self.node_coord.items():
            v[0] += -1*min_x
            v[1] *= -1
        
        # append [root.val, y_coord] -- at same x_coord position 
        for k,v in self.node_coord.items():
            output[v[0]].append([k, v[1]]) # [root,y_coord]
            
        # sort with y_coord per x_coord array
        for io in output:
            io.sort(key = lambda x:(x[1], x[0]))
        
        final_output = []
        for io in output:
            temp = []
            for i in io:
                temp.append(i[0])
            
            final_output.append(temp)
            
        return final_output
        
        
    def dfs(self, root, x, y):
        
        self.node_coord[root.val] = [x,y]
        if root.left is None and root.right is None:
            return
        
        if root.left:
            self.dfs(root.left, x-1, y-1)
        if root.right:
            self.dfs(root.right, x+1, y-1)
        
