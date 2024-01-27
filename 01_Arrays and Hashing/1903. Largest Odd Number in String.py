class Solution:
    def largestOddNumber(self, num: str) -> str:
        str_len=len(num)-1
        for i in range(str_len,-1,-1):
            truncated_str=num[:i+1]
            units=truncated_str[-1]
            if int(units)%2!=0:
                return truncated_str
        return ""    
