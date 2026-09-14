# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        ans=[]
        def solve(node,path):
            if node ==None:
                return 
            path+=str(node.val)
            if node.left==None  and node.right==None:
                ans.append(path)
                return 
            path+="->"
            solve(node.left,path)
            solve(node.right,path)
        solve(root,"")
        return ans

        