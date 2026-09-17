# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue=[root]
        count=0
        while queue:
            level=[]
            for i in range(len(queue)):
                node=queue.pop(0)
                level.append(node.val)
                if node.left!=None :
                    queue.append(node.left)
                if node .right!=None:
                    queue.append(node.right)
            if count%2==0:
                for i in level:
                    if i%2==0:
                        return False
                for i in range (1,len(level)):
                    if level[i]<=level[i-1]:
                        return False
            else:
                for i in level:
                    if i%2!=0:
                        return False
                for i in range(1, len(level)):
                    if level[i] >= level[i-1]:
                        return False
            count+=1
        return True
               
            
            


                

        