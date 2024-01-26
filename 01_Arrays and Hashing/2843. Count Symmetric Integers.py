class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def numOfDigit(self,numm:int)->bool:

            digits=0
            while numm:
                digits+=1
                numm=numm//10
            if digits%2==0:
                return True
            else:
                return False

        count=0

        for i in range(low,high+1):
            #even number
            if numOfDigit(self,i) and i>9:
                num_to_str=str(i)
                first=num_to_str[:len(num_to_str)//2]
                # print(first)

                #solving for first half
                sum_first=0
                for f in first:
                    sum_first+=int(f)
                last=num_to_str[len(num_to_str)//2:]
                

                #solving for last half
                last_sum=0
                for l in last:
                    last_sum+=int(l)
                
                if last_sum==sum_first:
                    print(last_sum,sum_first)
                    
                    count+=1
                         
        return count
