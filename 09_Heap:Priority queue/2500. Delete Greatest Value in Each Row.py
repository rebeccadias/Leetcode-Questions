import heapq
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        # making a new max heap grid 
        new_grid=[]
        result=0

        for row in grid:
            for ele in range(len(row)):
                row[ele]=-1*row[ele]
            heapq.heapify(row)
            new_grid.append(row)

        for i in range(len(new_grid[0])):
            comparing_max=[]
            for j in range(len(new_grid)):
                temp=-1*heapq.heappop(new_grid[j])
                comparing_max.append(temp)
            print(comparing_max)
            maxx=max(comparing_max)
            result+=maxx   
        return result      
