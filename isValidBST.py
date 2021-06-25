# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.checkMinMax(root, float("-inf"), float("inf"))
        
    def checkMinMax(self, root: TreeNode, mini: int, maxi: int) -> bool:
        if not root:
            return True
        
        if root.val <= mini or root.val >= maxi:
            return False
        
        return self.checkMinMax(root.left, mini, root.val) and self.checkMinMax(root.right, root.val, maxi)
        
        
#         if not root:
#             return True
        
#         leftValid, rightValid = False, False
        
#         if root.left:

#             leftValid = self.rightMost(root.left).val < root.val and root.left.val < root.val
#         else:
#             leftValid = True
            
#         if root.right:
#             rightValid = self.leftMost(root.right).val > root.val and root.right.val > root.val
#         else:
#             rightValid = True
        
#         return leftValid and rightValid and self.isValidBST(root.left) and self.isValidBST(root.right)
        
#     def leftMost(self, root: TreeNode) -> TreeNode:
#         while root.left is not None:
#             root = root.left
            
#         return root
    
#     def rightMost(self, root: TreeNode) -> TreeNode:
#         while root.right is not None:
#             root = root.right
            
#         return root