class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        hashmap=defaultdict(int)

        ans=0

        for n in nums:
                ans+=hashmap[n]
                hashmap[n]+=1
        return ans
  #the hashmap version reduces the time complexity from n2 to n 
