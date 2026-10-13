# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(node):
            if not node:
                return [True, 0]
            left = dfs(node.left)
            right = dfs(node.right)
            if left[0] == False or right[0] == False:
                return [False, 0]

            if abs(left[1]-right[1]) > 1:
                return [False, 0]
            
            return [True, max(left[1], right[1]) + 1]
        res = dfs(root)
        return res[0]


