class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        hashmap={}

        for word in words:
            for ele in word:
                if ele not in hashmap:
                    hashmap[ele]=1
                else:
                    hashmap[ele]+=1
        # print(hashmap)
        

        for k,v in hashmap.items():
            if v%len(words)!=0:
                return False
        return True

"""
The key strat here is to determine if each value in the hashmap is divisible by the lenght of array
"""
        
