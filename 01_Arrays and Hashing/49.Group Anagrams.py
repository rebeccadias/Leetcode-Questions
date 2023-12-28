class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        ans=[]
        hashmap={}
        for each_string in strs:
          sorted_string = "".join(sorted(each_string))
      
          if sorted_string not in hashmap:
            hashmap[sorted_string]=[each_string]  
          else:
            hashmap[sorted_string].append(each_string)
        for k,v in hashmap.items():
          ans.append(v)
        return ans
        
