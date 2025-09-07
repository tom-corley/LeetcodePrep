from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
       def dfs(root, ans):
            if not root:
                return 0, 0
            l, r = 0, 0
            if root.right:
                r = 1 + dfs(root.right, ans)[0]
            if root.left:
                l = 1 + dfs(root.left, ans)[1]
            ans[0] = max(ans[0], l, r)
            return l, r

       ans = [0]
       dfs(root, ans)
       print(ans)
       return ans[0]

    def longestZigZag2(self, root: Optional[TreeNode]) -> int:
        # Dfs adding each node to a stack of paths
        paths = []
        stack = [root]
        mx = 0
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                paths.append([node, 0, 0])
            if node.right:
                stack.append(node.right)
                paths.append([node, 0, 1])
        
        # Try each possible path
        while paths:
            node, length, d = paths.pop()
            if length > mx:
                mx = length
            if d == 0 and node.left:
                # Zig left
                paths.append([node.left, length + 1, 1])
            if d == 1 and node.right:
                # Zag right
                paths.append([node.right, length + 1, 0])

        return mx