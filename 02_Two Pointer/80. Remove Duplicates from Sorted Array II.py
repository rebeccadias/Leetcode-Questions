class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        count=1
        current=nums[0]

        for i in range(1,len(nums)):

            if nums[i]!=current:
                count=1
                current=nums[i]
            else:
                count+=1
                if count>2:
                    nums[i]="-"
        print(nums)
        
        i,j=0,0    
        while j<len(nums):

            if nums[i]!="-" and nums[j]!="-":
                i+=1
                j+=1
            elif nums[i]=="-" and nums[j]=="-":
                j+=1
            elif nums[i]=="-" and nums[j]!="-":
                #swapping operation
                nums[i]=nums[j]
                nums[j]='-'
                i+=1
        print(nums,i)
        # return i
        ans=0
        for ans in range(len(nums)):
            if nums[ans]=="-":
                return ans      
