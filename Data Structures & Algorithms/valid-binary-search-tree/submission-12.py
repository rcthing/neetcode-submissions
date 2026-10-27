# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ok = True
        def dfs(root, mini, maxi):
            nonlocal ok
            if not root or not ok:
                return

            if root.val <= mini or root.val >= maxi:
                ok = False
                return

            dfs(root.left, mini, root.val)
            dfs(root.right, root.val, maxi)

        dfs(root, float("-infinity"), float("infinity"))

        return ok

            