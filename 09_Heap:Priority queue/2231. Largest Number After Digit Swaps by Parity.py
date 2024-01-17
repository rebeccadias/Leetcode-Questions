import heapq
class Solution:
    def largestInteger(self, num: int) -> int:
      
        heap_even=[]
        heap_odd=[]
        indices=[]
        ans=[]
        result=''
        list_num=[int(x) for x in str(num)]
        for number in list_num:
            if number%2==0:
                heap_even.append(-1*number)
                indices.append('even')
            else:
                heap_odd.append(-1*number)
                indices.append('odd')
        
        heapq.heapify(heap_even)
        heapq.heapify(heap_odd)

        for indice in indices:
            if indice=="even":
                ans.append(-1*heapq.heappop(heap_even))
            else : 
                ans.append(-1*heapq.heappop(heap_odd))
        for i in ans:
            result+=str(i)
        return (int(result))




       
        


        
        
