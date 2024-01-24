# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxx=0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter(root):
            if root is None:
                return 0
            else:
                l=diameter(root.left)
                r=diameter(root.right)
                self.maxx=max(self.maxx,l+r)
                return max(l,r)+1     
        diameter(root)
        return self.maxx        
