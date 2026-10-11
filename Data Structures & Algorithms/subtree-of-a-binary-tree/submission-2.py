# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        subRoot_val = subRoot.val
        def dfs(node):
            nonlocal subRoot_val
            if not node:
                return None
            left = dfs(node.left)
            right = dfs(node.right)
            if left and left.val == subRoot_val:
                return left
            elif right and right.val == subRoot_val:
                return right
            if check_if_equal(node, subRoot):
                return node
            return None
            
        def check_if_equal(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False
            if p.val != q.val:
                return False
                
            return check_if_equal(p.left, q.left) and check_if_equal(p.right, q.right)

        res = dfs(root)
        if not res:
            return False
        
        return True
