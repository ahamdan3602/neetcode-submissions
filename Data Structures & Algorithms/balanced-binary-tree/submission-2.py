# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node: Optional[TreeNode]):
            if not node:
                return [True, 0]
            left = dfs(node.left) # [True, 1]
            right = dfs(node.right)

            if left[0] == False or right[0] == False:
                return [False, max(left[1], right[1])]

            if abs(left[1] - right[1]) > 1:
                return [False, max(left[1], right[1])]

            return [True, max(left[1], right[1]) + 1] # [True, 1]
        res = dfs(root)
        print(res)
        return res[0]

        