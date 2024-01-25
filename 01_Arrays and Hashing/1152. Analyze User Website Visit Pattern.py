from collections import defaultdict
from itertools import combinations
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        zipped_arr=[]

        for i in zip(username,timestamp,website):
            zipped_arr.append(i)
        # print(zipped_arr)

        ##sort on based of timestamp

        zipped_arr.sort(key=lambda x:x[1])

        # print(zipped_arr)

        hashmap=defaultdict(list)

        for j in zipped_arr:
            hashmap[j[0]].append(j[2])
        print(hashmap)

        combis=defaultdict(int)
        temp_list=[]
        for k,v in hashmap.items():
            temp_list=set(combinations(v,3))
            print(temp_list)
            for ele in temp_list:
                combis[ele]+=1
        print(combis)

        maxx_count=-1
        ans=[]

        for k,v in combis.items():
            if v>=maxx_count:
                maxx_count=v
        for k,v in combis.items():
            if v==maxx_count:
                ans.append(k)
        print(ans)
        if len(ans)>1:
            ans.sort()
        return ans[0]







        
