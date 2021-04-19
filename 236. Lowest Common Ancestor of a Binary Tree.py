
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        # pass one non-null value
        # if both non-null received -- pass root value
        if root is None:
            return None
        
        if p == root or q == root:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left != None and right != None:
            return root
        
        if left is None and right is None:
            return None
        
        if left is None:
            # right is not None
            return right
        
        return left
        
        """
        TLE
        # hashmap - root : child nodes
        root_child_nodes = {}
        main_root = root
        cur_root = root
        temp_root = root
        
        # bfs wise fill hashmap
        queue = [cur_root]
        while queue:
            a = queue.pop(0)
            child_nodes = []
            self.dfs_populate_hashmap(child_nodes, a)
            
            root_child_nodes[a] = child_nodes
            
            if a.left:
                queue.append(a.left)
            if a.right:
                queue.append(a.right)
            
        # print("root_child_nodes: ", root_child_nodes)
        
        anc = []
        for k,v in root_child_nodes.items():
            if p.val in v and q.val in v:
                anc.append(k)
                
        # print("anc: ", anc)
        
        root_length = [] # length should be less
        for a in anc:
            if a in root_child_nodes:
                root_length.append([a, len(root_child_nodes[a])])
        
        root_length.sort(key = lambda x:x[1])
        
        root_to_return_val = root_length[0][0]
        
        return root_to_return_val
        
        
    def dfs_populate_hashmap(self, array, root): # child nodes array
        
        if root and root.val not in array:
            array.append(root.val)
            
        if root.left: self.dfs_populate_hashmap(array, root.left)
        if root.right: self.dfs_populate_hashmap(array, root.right)
        
        """
	
