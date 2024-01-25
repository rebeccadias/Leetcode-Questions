import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        ans=""
        prev=""
        temp=[]
        hashmap={}
        max_heap=[]
        for i in s:
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
        # print(hashmap)

        for k,v in hashmap.items():
            heapq.heappush(max_heap,(-1*v,k))
        # print(max_heap)

        while max_heap:
            val,char=heapq.heappop(max_heap)
            value=-1*val

            # print(value,char)

            if value==0:
                continue
            elif char!=prev:
                ans+=char
                prev=char
                hashmap[char]-=1
                heapq.heappush(max_heap,(-1*(hashmap[char]),char))
                for ele in temp:
                    heapq.heappush(max_heap,ele)
                temp=[]
            else:
                temp.append((-1*value,char))
        
        if len(ans)==len(s):
            return ans
        else:
            return ""     
