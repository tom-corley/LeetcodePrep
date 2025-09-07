from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans = 1
        mx = float('-inf')
        q = deque()
        q.append([root, 1])
        layer_sum = 0
        current_level = 1

        while q:
            node, level = q.popleft()
            if level == current_level:
                layer_sum  += node.val
            else:
                if layer_sum > mx:
                    mx = layer_sum
                    ans = current_level
                current_level = level
                layer_sum = node.val
            if node.left:
                q.append([node.left, level + 1])
            if node.right:
                q.append([node.right, level + 1])
        if layer_sum > mx:
            ans = current_level
        return ans