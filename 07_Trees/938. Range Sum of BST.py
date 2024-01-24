# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.summation=0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def helper(root):
            if root is None:
                return 
            else:
                helper(root.left)
                if low <= root.val <=high :
                    self.summation+=root.val
                    
                helper(root.right)
        helper(root)
        return self.summation

        
