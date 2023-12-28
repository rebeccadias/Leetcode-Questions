class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            if nums[i]>0:
                break
            while j<k:
                
                if (nums[i]+nums[j]+nums[k])==0:
                    if ([nums[i], nums[j], nums[k]]) not in result:
                        result.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                
                    # while j < k and nums[j] == nums[j + 1]:  # Skip duplicate 'j'
                    #     j += 1
                    # while j < k and nums[k] == nums[k - 1]:  # Skip duplicate 'k'
                    #     k -= 1
                elif (nums[i]+nums[j]+nums[k])<0:
                    j+=1
              
                elif (nums[i]+nums[j]+nums[k])>0:
                 
                    k-=1
        return result


        """
        If the current number nums[i] is positive, since the array is sorted, there's no need to continue because you won't be able to find three numbers that sum up to zero.


        question:
        Why do we increment BOTH j AND k. Wouldn't this cause us to skip over potential valid triplets because it increments two indices at once? My intuition is that we should only increment EITHER j OR k
        answer:
        
Suppose the current indices (i,j,k) create a triplet. Now you are asking that (i,j+1,k) or (i,j,k-1) could have made a triplet.

But in the first case (j+1) this would give an answer greater than the sum and vice versa for k-1. That means incrementing only one pointer is useless. It’s better and more efficient to change both pointers after finding a triplet.If you carefully understand the algorithm you will realise that every type of triplet is only being considered once.

        """
        
