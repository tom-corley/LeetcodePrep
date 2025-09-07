from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        ans = 0
        stack = []
        stack.append([root, root.val])
        stack2 = [root]
        while stack2:
            node = stack2.pop()
            if node.left:
                stack.append([node.left, node.left.val])
                stack2.append(node.left)
            if node.right: 
                stack.append([node.right, node.right.val])
                stack2.append(node.right)



        while stack:
            node, path_sum = stack.pop()
            if path_sum == targetSum:
                ans += 1
            if node.left:
                # Extend left 
                stack.append([node.left, path_sum + node.left.val])
            if node.right:
                # Extend right 
                stack.append([node.right, path_sum + node.right.val])
        return ans