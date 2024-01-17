class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        nums_set=set(nums)
        if 0 in nums_set: nums_set.remove(0)
        return len(nums_set)
