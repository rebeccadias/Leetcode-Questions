class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        rows=len(matrix)
        cols=len(matrix[0])

       
     
        ans=list()
    
        # ans = [[None for _ in range(rows)] for _ in range(cols)]

        # Initialize ans with dimensions cols x rows
        ans = []
        for _ in range(cols):
            row = [None] * rows
            ans.append(row)
    

        for r in range(rows):
            for c in range(cols):
                # print(matrix[r][c])
                ans[c][r]=matrix[r][c]
   
        return ans
        
