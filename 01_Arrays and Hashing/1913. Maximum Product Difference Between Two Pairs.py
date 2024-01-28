    # version 2 the time complexity is O(n)
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        maximum,prevmaxi=0,0
        mini,pmini=float('inf'),float('inf')
        for num in nums:
            if num>maximum:
                prevmaxi=maximum
                maximum=num
            elif num>prevmaxi:
                prevmaxi=num
            
            if num<mini:
                pmini=mini
                mini=num
            elif num<pmini:
                pmini=num

        print(maximum,prevmaxi)
        print(pmini,mini)
        return abs((maximum*prevmaxi)-(mini*pmini))
    # version 1 the time complexity is O(nlogn)

        # nums.sort()
        # print(nums)

        # first,second=nums[0],nums[1]
        # last,slast=nums[-1],nums[-2]

        # return abs((first*second)-(last*slast))

