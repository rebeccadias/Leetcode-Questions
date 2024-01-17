class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        ans=[]
        while nums:
            min_alice=min(nums)
            nums.remove(min_alice)

            min_bob=min(nums)
            nums.remove(min_bob)
           
            ans.append(min_bob)
            ans.append(min_alice)
            
        return ans
