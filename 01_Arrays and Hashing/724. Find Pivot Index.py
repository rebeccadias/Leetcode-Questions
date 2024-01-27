class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        temp_arr_forward=[nums[0]]

        backward=nums[::-1]
        temp_arr_back=[backward[0]]

        for i in range(1,len(nums)):
            temp_arr_forward.append(temp_arr_forward[i-1]+nums[i])

        for i in range(1,len(nums)):
            temp_arr_back.append(temp_arr_back[i-1]+backward[i])
        
        temp_arr_back=temp_arr_back[::-1]
        
        for i in range(len(temp_arr_forward)):
            if temp_arr_forward[i]==temp_arr_back[i]:
                return i
        return -1
""" idea is to use prefix sum logic """
