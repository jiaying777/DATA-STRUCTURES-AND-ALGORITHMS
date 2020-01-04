# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            a=self.invertTree(root.right)
            b=self.invertTree(root.left)
            root.left, root.right = a, b
        return root
