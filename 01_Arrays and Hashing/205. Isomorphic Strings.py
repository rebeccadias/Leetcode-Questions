"""we need to match from both the sides here : why ? code fails for testcase badc baba"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        hashmap_st={}
        hashmap_ts={}

        if len(s)!=len(t):
            return False
        
        for i in range(len(s)):
            if s[i] not in hashmap_st:
                hashmap_st[s[i]]=t[i]
            else:
                if hashmap_st[s[i]]!=t[i]:
                    return False
            

        for i in range(len(t)):
            if t[i] not in hashmap_ts:
                hashmap_ts[t[i]]=s[i]
            else:
                if hashmap_ts[t[i]]!=s[i]:
                    return False
        return True
      
