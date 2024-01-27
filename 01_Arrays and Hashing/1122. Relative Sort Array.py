class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        ans=[]
        remaining=[]

        #creating hashmap from arr1
        hashmap_arr1={}
        for ele in arr1:
            if ele not in hashmap_arr1:
                hashmap_arr1[ele]=1
            else:
                hashmap_arr1[ele]+=1
        
        for arr in arr2:
            #store the value/count here
            count=hashmap_arr1[arr]
            #run the loop until the count 
            for i in range(count):
                ans.append(arr)
        
        for element in arr1:
            if element not in ans:
                remaining.append(element)
        remaining.sort()

        for remain in remaining:
            ans.append(remain)
        return ans
        
        
        
        
            
        
        

                





        

   

        
