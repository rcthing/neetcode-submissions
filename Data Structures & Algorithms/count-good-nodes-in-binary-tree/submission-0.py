# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        nr = 0
        def dfs(node, maxi):
            nonlocal nr
            if not node:
                return
            
            if node.val >= maxi:
                nr += 1
                maxi = node.val

            dfs(node.left, maxi)
            dfs(node.right, maxi)

        dfs(root,-101)

        return nr


            