#using min-heap to record the distance

import heapq 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l=[]
        ans=[]
        for point in points:
            x,y=point[0],point[1]
            x_square=x*x
            y_squre=y*y
            root=math.sqrt(x_square+y_squre)
            l.append((root,[x,y]))
        heapq.heapify(l)
  
        while k>=1:
            minimum=heapq.heappop(l)
            ans.append(minimum[1])
            k-=1
           
        return(ans)

            
   

           
        return 0
            


        
