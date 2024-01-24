# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swap(root):

            if root is None :
                    return None
            else:
                root.right,root.left=swap(root.left),swap(root.right)
                return root
        return swap(root) 
        

        """
        in recursion we have a base case which stops the execution
        in the else part we have a case which calls the recursive function again 
        we need to return something from the recursive function to keep the control flow going 
        """
