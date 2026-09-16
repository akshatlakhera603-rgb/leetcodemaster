# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def sol(root):
            if root == None:
                return True
            if root.left!=None:
                if root.left.val!=root.val:
                    return False
            if root.right!= None:
                if root.right.val!=root.val:
                    return False
            return sol(root.left) and sol(root.right)
            
        return sol(root)
        
        
        