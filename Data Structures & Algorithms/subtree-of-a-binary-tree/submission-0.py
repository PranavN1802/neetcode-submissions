# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            if t1 is None or t2 is None: 
                return t1 is t2
            
            return ((t1.val == t2.val) and (isSame(t1.left,t2.left)) and (isSame(t1.right,t2.right)))

        if root is None:
            return False

        return (isSame(root, subRoot) or
                self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))