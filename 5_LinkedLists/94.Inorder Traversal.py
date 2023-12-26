# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:


        stack=[]
        result=[]
        new_root=root
        

        while stack or new_root:
    
            while new_root:
           
                stack.append(new_root)
                new_root=new_root.left
        
            new_root=stack.pop()
            result.append(new_root.val)
            
            new_root = new_root.right

        return result
    
            
            

        
