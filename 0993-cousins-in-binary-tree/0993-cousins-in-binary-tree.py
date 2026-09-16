# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode | None, x: int, y: int) -> bool:
        xparent1=None
        yparent1=None
        queue=[root]
        while queue:
            size=len(queue)
            xparent=None
            yparent=None
            for i in range(size):
                node=queue.pop(0)
                if node.left:
                    if node.left.val==x:
                        xparent=node
                    if node.left.val==y:
                        yparent=node

                    queue.append(node.left)
                if node.right:
                    if node.right.val==x:
                        xparent=node
                    if node.right.val==y:
                        yparent=node
                    queue.append(node.right)
                
            if xparent!=None and yparent!=None:
                return xparent!=yparent
            if xparent!= None or yparent!=None:
                return False
      
        return False
        