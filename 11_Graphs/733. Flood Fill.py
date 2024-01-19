class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        directions={(-1,0),(0,-1),(1,0),(0,1)}
        prevcol = image[sr][sc]
        queue=[(sr,sc)]
        image[sr][sc]=color
        while queue:
            x,y=queue.pop(0)

            for i,j in directions:
                newx,newy=x+i,y+j
                if 0<=newx<len(image) and 0<=newy<len(image[0]) and image[newx][newy]!=color:
                    # print(image[x][y],"iniy")
                    if image[newx][newy]==prevcol:
                        print(newx,newy)
                        queue.append((newx,newy))
                        image[newx][newy]=color
        return image     
