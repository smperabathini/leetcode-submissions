# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def diameter(node):
            nonlocal res
            if not node:
                return 0
            else:
                left = (diameter(node.left))
                right = diameter(node.right)
                temp = left + right
                res = max(temp,res)
                return 1 + max(left,right)
            
        diameter(root)
        return res

            

