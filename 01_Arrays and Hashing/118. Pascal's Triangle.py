class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows==0:
            return [[]]
        elif numRows==1:
            return [[1]]

        ans=[[1],[1,1]]

        for i in range(2,numRows):
            #length of the last element of ans
            curr_arr_len=ans[i-1]
            result=[]  
            for j in range(len(curr_arr_len)+1):
                
                if j==0:
                    result.append(1)
                elif j==len(curr_arr_len):
                    result.append(1)
                else:
                    result.append(curr_arr_len[j]+curr_arr_len[j-1])
            ans.append(result) 
            print(ans)
        return and 

# 119. Pascal's Triangle.py

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        ans=[[1],[1,1]]

        if rowIndex==0:
            return ans[0]
        elif rowIndex==1:
            return ans[1]

        for i in range(2,rowIndex+1):

            curr_array=ans[i-1]
            result=[]
            for j in range(len(curr_array)+1):
                if j==0:
                    result.append(1)
                elif j==len(curr_array):
                    result.append(1)
                else:
                    result.append(curr_array[j]+curr_array[j-1])
            ans.append(result)
        return ans[-1]
   
