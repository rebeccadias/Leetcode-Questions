class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        # first we make a hashmap of the arr 
        hashmap={}
        

        for a in arr:
            if a not in hashmap:
                hashmap[a]=1
            else:
                hashmap[a]+=1
        # print(hashmap)

        # now make a set of all the values out of the hashmap
        sett=set()
        for k,v in hashmap.items():
            sett.add(v)
        if len(sett)==len(hashmap):
            return True
        else:
            return False
    



        
