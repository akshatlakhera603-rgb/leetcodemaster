class Solution:
    def longestUnivaluePath(self, root):
        ans = 0
        def solve(node):
            nonlocal ans
            if node == None:
                return 0
            left = solve(node.left)
            right = solve(node.right)
            if node.left != None and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right != None and node.right.val == node.val:
                right += 1
            else:
                right = 0
            ans = max(ans, left + right)
            return max(left, right)
        solve(root)
        return ans