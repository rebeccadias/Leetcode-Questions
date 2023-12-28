class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """ time complexity for the below code is O(n^2) 18/22 which is not whats expected so we do it using prefix sum walla method"""
        #method 1 
        # ans=[]
        # for i in range(len(nums)):
        #     prod=1
        #     for j in range(len(nums)):
        #         if i==j:
        #             continue
        #         else:
        #             prod*=nums[j]
        #     ans.append(prod)
        # return ans
