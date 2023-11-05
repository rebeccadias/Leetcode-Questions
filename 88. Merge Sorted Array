https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
    # Set pointers for nums1 and nums2
        p1=m-1
        p2=n-1

        p=m+n-1 # Set pointer for nums1's actual end

        while p1>=0 and p2>=0:

            if nums1[p1]<nums2[p2]:
                nums1[p]=nums2[p2]
                p2-=1
            else:
                nums1[p]=nums1[p1]
                p1-=1
            p-=1
        # If there are elements left in nums2, copy them over to nums1
        nums1[:p2+1] = nums2[:p2+1]
        

