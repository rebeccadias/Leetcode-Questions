class Solution:
    def addStrings(self, num1: str, num2: str) -> str:


        carry=0
        ans=""
        num1=num1[::-1]
        num2=num2[::-1]

        max_len=max(len(num1),len(num2))

        if max_len==len(num1):
            difference=len(num1)-len(num2)
            num2=num2+("0"*difference)
        else:
            difference=len(num2)-len(num1)
            num1=num1+("0"*difference)
        
        for n in range(max_len):
            val=int(num1[n])+int(num2[n])+carry
            
            if val > 9:
                carry=1
                ans+=str(val%10)
            else:
                carry=0
                ans+=str(val)
        if carry ==1:
            ans+="1"
        return ans[::-1]
        
