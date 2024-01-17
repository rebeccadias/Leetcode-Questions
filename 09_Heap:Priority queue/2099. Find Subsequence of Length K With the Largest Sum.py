import heapq
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        ans=[]
        heapq.heapify(heap)
        for index,element in enumerate(nums):
            heapq.heappush(heap,(element,index))
        while len(heap)!=k:
            heapq.heappop(heap)
        heap.sort(key=lambda x:x[1])
        for k in range(len(heap)):
            ans.append(heap[k][0])
        return ans
       
