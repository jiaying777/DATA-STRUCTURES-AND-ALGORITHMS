# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        temp = 0
        if root and root.val >= L and root.val <= R:
            temp += root.val
        if root.left:
            temp += self.rangeSumBST(root.left,L,R)
        if root.right:
            temp += self.rangeSumBST(root.right,L,R)
        return temp
