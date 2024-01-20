class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left=0
        right=len(nums)-1
        # if len(nums) == 1:
        #     if nums[0] >= target:
        #         return 0
        #     else:
        #         return 1
        while left<=right:
            
            mid=(left+right)//2
            if nums[mid] == target:
                return mid
            if target>nums[mid]:
                left=mid+1
            else:
                right=mid-1
        return left



        
