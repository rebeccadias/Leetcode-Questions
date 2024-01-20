#method 2
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap={}
        stack=[nums2[0]]
        ans=[]
        for i in range(1,len(nums2)):

            # print(stack)
            if nums2[i]>stack[-1]:
                while stack and nums2[i]>stack[-1]:
                    popped_element=stack.pop()
                    hashmap[popped_element]=nums2[i]
                stack.append(nums2[i])
            else:
                stack.append(nums2[i])
        while stack:
            hashmap[stack.pop()]=-1
        print(hashmap)

        for i in range(len(nums1)):
            if nums1[i] in hashmap:
                ans.append(hashmap[nums1[i]])
            
        return ans



        """non stack approach """
        # result=[]

        # for i in range(len(nums1)):
        #     if nums1[i] in nums2:
        #         index=nums2.index(nums1[i])
        #         min_element=nums2[index]
        #         print(index,min_element)
        #         for j in range(index,len(nums2)):
        #             if min_element < nums2[j]:
        #                 result.append(nums2[j])
        #                 break
        #         else:
        #             result.append(-1) 
        # return result

        
