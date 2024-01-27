# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def cousin(root,depth,value,parent):
            
            if root is None:
                return (0,-1)
            else:
                if root.val == value:
                    return (depth,parent)
                else:
                    l=cousin(root.left,depth+1,value,root)
                    r=cousin(root.right,depth+1,value,root)
                    if l[0] > r[0]:
                        return l[0],l[1]
                    else:
                        return r[0],r[1]
                    # return (max(l[0],r[0]),root)
        depth1,par1 = cousin(root,0,x,-1)
        depth2,par2 = cousin(root,0,y,-1)
        # print(depth1,par1)
        # print(depth2,par2)
        if par1!=par2 and depth1==depth2:
            return True
        else:
            return False    
