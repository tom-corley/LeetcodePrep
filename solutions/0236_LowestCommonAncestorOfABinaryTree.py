# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        
        return left or right


    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def search(node, val):
            if not node:
                return False
            if node.val == val:
                return True
            return search(node.left, val) or search(node.right, val)
        
        def rcv(tree, p, q):
            if tree.left and search(tree.left, p.val) and search(tree.left, q.val):
                return rcv(tree.left, p, q)
            elif tree.right and search(tree.right, p.val) and search(tree.right, q.val):
                return rcv(tree.right, p, q)
            else:
                return tree
        
        return rcv(root, p, q)
