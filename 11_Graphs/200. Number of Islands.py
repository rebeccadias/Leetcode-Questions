class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def bfs(queue,grid) :
            

            while queue:
                #we put the coordinates in the queue, not the element, in the Q we are interested in the cords

                x,y=queue.pop(0)
                visited.add((x,y))
                # print(visited)

                grid[x][y]="0"
                # print(x,y)

                for dx,dy in directions:
                    new_x,new_y=x+dx,y+dy
                    # print(new_x,new_y)
                    if new_x>=0 and new_x<m and new_y>=0 and new_y<n and grid[new_x][new_y]=="1" and (new_x,new_y) not in visited:
                        queue.append((new_x,new_y))
                        visited.add((new_x,new_y))

        directions=[(0,-1),(0,1),(1,0),(-1,0)] 
        m=len(grid)
        n=len(grid[0])
        
        #we can move in four directions, sometimes in other questions we might have to move diagonally as well
        islands=0
        queue=[] 
        visited = set()
      
    
        #we put the coordinates of the first element in the grid irrespective of the 1 or 0 because we do not want the code not to enter the loop only so we initialize it with something atleast

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    queue.append((i,j))
                    bfs(queue,grid)
                    islands+=1

           
        return islands
           
           
       
        """
        the first approach was not to use the visited set but I got a TLE while I was doing it because repeated elements were entering the queue so I put a check on that 
        BFS uses Queue, Imagine that each i and j is a node in a tree and we visit the child. so we do breadth my breadth  
    """


                    






        


        
