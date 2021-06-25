# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    solutions = []
    
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.generateTreeLowToHigh(1, n)
        
        
    def generateTreeLowToHigh(self, low: int, high: int) -> List[TreeNode]:
        if high < low:
            return [None]
        
        solutions = []
        for i in range(low, high + 1):
            solutions += [TreeNode(i, left, right) for left in self.generateTreeLowToHigh(low, i-1) for right in self.generateTreeLowToHigh(i+1, high)]
        return solutions