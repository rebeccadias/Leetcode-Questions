import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap=[]
        ans=[]

        for matt in range(len(mat)):
            countof=mat[matt].count(1)
           
            print(countof)
            # # heapq.heappush(heap,[countof,matt])

            heap.append([countof,matt])
        heapq.heapify(heap)
        
        for k in range(k):
            print(k)
            temp=heapq.heappop(heap)
            ans.append(temp[1])
        return ans
       
