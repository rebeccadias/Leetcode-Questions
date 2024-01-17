import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        max_heap=[]
        hm={}
        result=[]

        #create Hashmap
        for i in nums:
          if i not in hm:
              hm[i]=1
          else:
              hm[i]+=1

        #create Max heap out of the hashmap
        for key_1,value_1 in hm.items():
          max_heap.append((key_1,-value_1))
        print(max_heap)
        heapq.heapify(max_heap)
     
        #pop the K elements from the Max_heap
        for i in range(k):
          key,value = heapq.heappop(max_heap)
          result.append(key)
        return result
