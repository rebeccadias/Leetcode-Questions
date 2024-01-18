
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap={}

        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]]=[1,i]
            else:
                count=hashmap[s[i]][0]+1
                hashmap[s[i]]=[count,i]
        # print(hashmap)
        prev_index=float('inf')
        for k,v in hashmap.items():
            occurance,index=v
            if occurance==1:
                if prev_index>index:
                    prev_index=index
        return prev_index if prev_index != float('inf') else -1
       
