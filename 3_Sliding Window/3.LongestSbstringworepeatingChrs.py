class Solution(object):
    def lengthOfLongestSubstring(self, s):
        charSet=set()

        l=0
        res=0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res=max(res,r-l+1)
        return res
       
       
"""max(res, r - l + 1): The max function is used to determine the maximum value between the current res and the length of the current substring (r - l + 1). It effectively compares the length of the current substring with the length of the longest substring found so far (res) and selects the greater of the two."""
    
            