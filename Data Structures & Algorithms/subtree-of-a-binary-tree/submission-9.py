# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ok = 0
        def same_tree(r1, r2):
            if not r1 and not r2:
                return True
            
            if r1 and r2 and r1.val == r2.val:
                return same_tree(r1.left, r2.left) and same_tree(r1.right, r2.right)
            else:
                return False

        def dfs(r1, r2):
            if not r1:
                return False
            if same_tree(r1,r2):
                return True
            return dfs(r1.left,r2) or dfs(r1.right,r2)
            
        return dfs(root, subRoot)

