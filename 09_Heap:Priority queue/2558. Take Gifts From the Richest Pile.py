import heapq
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for ele in range(len(gifts)):
            gifts[ele]=-1*gifts[ele]
        heapq.heapify(gifts)

        for i in range(k):
            print(i)
            number=-1*heapq.heappop(gifts)
            print(number)
            root=math.sqrt(number)
            print(root)
            floorroot=math.floor(root)
            print(floorroot)
            heapq.heappush(gifts,-1*floorroot)
        if gifts:
            for ele in range(len(gifts)):
                gifts[ele]=-1*gifts[ele]
        return sum(gifts)
        

        
