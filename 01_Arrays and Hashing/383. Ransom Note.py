class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap={}

        for element in magazine:
            if element not in hashmap:
                hashmap[element]=1
            else:
                hashmap[element]+=1
        
        for every_char in ransomNote:
            if every_char in hashmap and hashmap[every_char]>0:
                hashmap[every_char]-=1
            else:
                return False
        return True       
