# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans=0
        queue=[root]
        while queue:
            count=len(queue)
            for i in range(len(queue)):
                node=queue.pop(0)
                if i==0:
                    ans=node.val
                if node.left!=None:
                    queue.append(node.left)
                if node.right!=None :
                    queue.append(node.right)
        return ans
        