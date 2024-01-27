class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for x in range(len(nums)+1):
            count_x=0
            for num in nums:
                if num>=x:
                    count_x+=1
            # print(x,count_x)
            if x==count_x:
                return x
        return -1     
