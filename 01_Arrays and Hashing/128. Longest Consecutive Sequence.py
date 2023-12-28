class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        hashmap={}
        count=0
        maxcount=0
        # A solution
        for num in nums:
            # print(num)
            # print (hashmap)
            first,last=num,num
            if num in hashmap:
                first,last=hashmap[num]
            if (num+1) in hashmap:
                if hashmap[num+1][1]>last:
                    last=hashmap[num+1][1]
                if hashmap[num+1][0]<first:
                    first=hashmap[num+1][0]
            if (num-1) in hashmap:
                if hashmap[num-1][0]<first:
                    first=hashmap[num-1][0]
                if hashmap[num-1][1]>last:
                    last=hashmap[num-1][1]
            hashmap[num]=[first,last]
            if hashmap[last][0] > first:
                hashmap[last][0]=first
            if hashmap[first][1]<last:
                hashmap[first][1]=last

        
        for k,v in hashmap.items():
            if count>maxcount:
                maxcount=count
            count=v[1]-v[0]
        return (maxcount+1)
     
