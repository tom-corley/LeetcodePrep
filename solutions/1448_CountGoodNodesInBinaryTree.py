from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(biggest, node, ans):
            if not node:
                return
            if node.val >= biggest:
                ans[0] += 1
            dfs(max(node.val, biggest), node.left, ans)
            dfs(max(node.val, biggest), node.right, ans)
        ans = [0]
        dfs(float('-inf'), root, ans)
        return ans[0]