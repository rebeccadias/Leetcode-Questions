class Solution:
    def isHappy(self, n: int) -> bool:
        
        numbersSet=set()
        def divide_number_sqaure(number):
            ans=0
            while number>0:
                right_most_digit=number%10
                number=number//10
                sqaured=right_most_digit**2
                ans+=sqaured
            return ans
        
        while n!=1:                
            if n in numbersSet:
                return False
            numbersSet.add(n)
            n=divide_number_sqaure(n)
            
        return True
