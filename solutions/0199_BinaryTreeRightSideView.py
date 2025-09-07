from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        ans = []
        q = deque()
        q.append([root, 0])
        layer = []
        current_level = 0
        while q:
            node, level = q.popleft()
            if level == current_level:
                layer.append(node.val)
            else:
                ans.append(layer.pop())
                current_level = level
                layer = [node.val]
            if node.left:
                q.append([node.left, level + 1])
            if node.right:
                q.append([node.right, level + 1])
        ans.append(layer.pop())
        return ans