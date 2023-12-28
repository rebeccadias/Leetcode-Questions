class Solution:
    def isValid(self, s: str) -> bool:

        # top=-1   # index of the topmost element
      
        # stack=[]

        # for element in s:
        #     # print(stack,top)
        #     if element == "(" or element == "{" or element == "[":
        #         stack.append(element)
        #     else:
        #         if (element ==")" or element =="}" or element =="]") and len(stack)!=0 :
        #             if  (element ==")" and stack[-1] =="(" ) or (element =="}" and stack[-1] =="{") or (element =="]" and stack[-1] =="[" ):
        #                 stack.pop()
        #             else:
        #                 return False
        #         else:
        #             return False
        # return True if len(stack) == 0 else False
        stack=[]

        for element in s:
            # print(stack,top)
            if element in ["(","{","["]:
                stack.append(element)
            else:
                if element in [")","}","]"] and len(stack)!=0 :
                    if  (element ==")" and stack[-1] =="(" ) or (element =="}" and stack[-1] =="{") or (element =="]" and stack[-1] =="[" ):
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return True if len(stack) == 0 else False
               
                




    
        