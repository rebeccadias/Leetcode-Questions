"""Algo Mid term question which you got wrong  ;( """
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for ele in range(len(nums)):
            nums[ele]=-1*nums[ele]
        heapq.heapify(nums)

        for i in range(k):
            last_popped=heapq.heappop(nums)
        return -1*last_popped
