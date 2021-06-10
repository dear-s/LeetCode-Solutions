
class BSTIterator:

    def __init__(self, root: TreeNode):
        
        self.root = root
        self.traversal = []

        if root is not None:
            queue = [root]

            while queue:
                a = queue.pop(0)
                self.traversal.append(a.val)
                if a.left:
                    queue.append(a.left)
                if a.right:
                    queue.append(a.right)

        self.traversal.sort()
        
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        
        if len(self.traversal) == 0:
            return
        
        ret = self.traversal.pop(0)
        return ret
        
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if len(self.traversal) > 0:
            return True
        else:
            return False
        
