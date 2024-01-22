'''

Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"

'''

#converts str to int returns int as the ans 
def Solution(num1,num2):
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
        ans+=1
    return ans[::-1]

print(Solution("0","0"))
    
