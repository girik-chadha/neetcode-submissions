# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both nodes are null, so they are the same
        if not p and not q:
            return True
        
        # One is null but the other isn't, so they are different
        if not p or not q:
            return False
        
        # The values are different
        if p.val != q.val:
            return False
        
        # Check if both left subtrees are identical AND right subtrees are identical
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)