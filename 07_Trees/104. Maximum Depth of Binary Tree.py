# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # print(root)
        if root is None:
            return 0
        depth=1
        stack=[[root,depth]]

        while len(stack)!=0 :
           
            new_root,depth=stack.pop(0)
            if new_root.left is not None:
                stack.append([new_root.left,depth+1])
            if new_root.right is not None:
                stack.append([new_root.right,depth+1])
           
        return depth
            

"""
maintain a stack ... used the iterative approach in this question instead of recursion 
"""


        
