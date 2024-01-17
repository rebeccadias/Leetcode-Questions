import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #making max-heap
        for n in range(len(stones)):
            stones[n]=-1*stones[n]
        print(stones)
        heapq.heapify(stones)
        
        while len(stones)>=1:
            if len(stones)==1: return -1*stones[0]
            max_1=-1*heapq.heappop(stones)
            max_2=-1*heapq.heappop(stones)
            if max_1==max_2:
                continue
            elif max_1!=max_2:
                new_y=max_1-max_2
                heapq.heappush(stones,-1*new_y)
        if stones:
            return (-1*stones[0])
        else:
            return 0
        

        
