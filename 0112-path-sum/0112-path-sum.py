# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def path(root,target):
            if root==None:
                return False
            if root.left==None and root.right==None:
                return target==root.val
            left=path(root.left,target-root.val)
            right=path(root.right,target-root.val)
            return left or right
        return path(root,targetSum)
        