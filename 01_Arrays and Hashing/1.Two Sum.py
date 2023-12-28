class Solution(object):
    def twoSum(self, nums, target):
#hashmap approach
        hash_map={}
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff not in hash_map:
                hash_map[nums[i]]=i
                
            else:
                return [i,hash_map[diff]]
        print(hash_map)

      


      #brute force approach
        # index1=[]
        # for i in range(len(nums)): 
        #     for j in range(i+1,len(nums)):
        #         if (target-nums[i])==nums[j]:
        #             index1.append(i)
        #             index1.append(j)
        # return index1



      