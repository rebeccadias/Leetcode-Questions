import heapq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans=[]
        heap=[]
        hashmap={}
        k=1
        for i in score:
            heap.append(-i)
        heapq.heapify(heap)
        while heap:
            hashmap[-1*(heapq.heappop(heap))]=k
            k+=1
        for s in score:
            if hashmap[s]==1:
                ans.append("Gold Medal")
            elif hashmap[s]==2:
                ans.append("Silver Medal")
            elif hashmap[s]==3:
                ans.append("Bronze Medal")
            else:
                ans.append(str(hashmap[s]))
        return ans
            
            
                

            




       





        
