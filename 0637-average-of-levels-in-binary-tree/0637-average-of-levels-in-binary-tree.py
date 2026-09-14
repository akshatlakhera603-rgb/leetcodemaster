# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root==None:
            return 0
        queue=[root]
        ans=[]
        while queue:
            average=0
            count=len(queue)
            for i in range (len(queue)):
                node=queue.pop(0)
                average+=node.val
                if node.left!=None:
                    queue.append(node.left)
                if node.right!=None:
                    queue.append(node.right)
            average/=count
            ans.append(average)
        return ans
        
