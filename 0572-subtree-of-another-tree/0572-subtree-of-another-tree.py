# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def issame(p,q):
            if p==None and q==None :
                return True
            if p==None or q==None:
                return False
            left=issame(p.left,q.left)
            right=issame(p.right,q.right)
            return p.val==q.val and left and right
        def search(root):
            if root==None:
                return False
            if issame(root,subRoot):
                return True
            left=search(root.left)
            right=search(root.right)

            return left or right
        return search(root)
            

        