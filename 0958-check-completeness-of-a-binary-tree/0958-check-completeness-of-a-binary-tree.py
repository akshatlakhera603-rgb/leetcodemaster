# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode | None) -> bool:
        queue=[root]
        found=False
        while queue:
            node=queue.pop(0)
            if node==None:
                found=True
                continue
            if found:
                return False
            queue.append(node.left)
            queue.append(node.right)
        return True        