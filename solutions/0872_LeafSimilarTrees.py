from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Post order traversal with only leaves
        def post_order(node, arr):
            leaf = True
            if node.left:
                leaf = False
                post_order(node.left, arr)
            if node.right:
                leaf = False
                post_order(node.right, arr)
            
            if leaf:
                arr.append(node.val)
        
        arr1 = []
        arr2 = []
        post_order(root1, arr1)
        post_order(root2, arr2)
        return arr1 == arr2