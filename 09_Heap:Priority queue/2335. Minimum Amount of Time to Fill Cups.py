"""Method1:
Sort the list. Every time take two max numbers and decrement them by one. Aslo increment count by one. If only one non zero element present then add that number to count and return the count. If all are zero then return count.
Method2:make max heap, pop2 do the calculations, push the remaining numbers after doing the calculations"""
import heapq
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        count=0

        for i in range(len(amount)):
            amount[i]=-1*amount[i]
        heapq.heapify(amount)

        while len(amount)>1:
            max1=-1*heapq.heappop(amount)
            max2=-1*heapq.heappop(amount)
            if max1 and max2: 
                max1-=1
                max2-=1
                count+=1
            if max1:
                heapq.heappush(amount,-1*max1)
            if max2:
                heapq.heappush(amount,-1*max2)
        if amount:
            return count-amount[0] 
            #amount is already multiplied by minus , so we do - of - which equals to +
        else:
            return count



        

           

        







        
