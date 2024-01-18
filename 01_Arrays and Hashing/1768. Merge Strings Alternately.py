class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=''
        lengthofsmall=min(len(word1),len(word2))
        
        for i in range(lengthofsmall):
            ans+=word1[i]
            ans+=word2[i]
        if len(word1)>len(word2):
            ans+=word1[len(word2):]
        else:
            ans+=word2[len(word1):]
        return ans
