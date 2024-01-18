class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        ans =[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                element="FizzBuzz"
            elif i%3==0:
                element="Fizz"
            elif i%5==0:
                element="Buzz"
            else:
                element=str(i)
            ans.append(element)
        return ans
