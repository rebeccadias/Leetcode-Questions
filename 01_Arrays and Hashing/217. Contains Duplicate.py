class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashmap={}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]]=1
            else:
                hashmap[nums[i]]+=1
        for k,v in hashmap.items():
            if v >=2:
                return True
        return False
