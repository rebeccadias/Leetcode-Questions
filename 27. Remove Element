class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        p1 = 0  # Pointer to place non-val elements
        for p2 in range(len(nums)):  # Pointer to scan through the list
            if nums[p2] != val:
                nums[p1] = nums[p2]
                p1 += 1
        return p1
