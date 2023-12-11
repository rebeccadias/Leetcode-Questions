class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        clean_string=""

        for each_char in s:
            if each_char.isalnum():
                clean_string+=each_char.lower()
        print(clean_string)
        if len(clean_string)==1:
            return True
        

        #method 1 
        # reversed_clean_string=clean_string[::-1]
        # if reversed_clean_string == clean_string:
        #     return True
        # else:
        #     return False
        

        #method 2 
        reversed_clean_string=""
        i=0
        j=len(clean_string)-1
        while(i<j):
            if clean_string[i]!=clean_string[j]:
                return False
            i+=1
            j-=1
        return True
        
        

