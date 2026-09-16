# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        l1=[]
        l2=[]
        def sol(root,li):
            if root == None:
                return False
            if root.left==None and root.right==None:
                li.append(root.val)
            sol(root.left,li)
            sol(root.right,li)
        sol(root1,l1)
        sol(root2,l2)
        return l1==l2
        