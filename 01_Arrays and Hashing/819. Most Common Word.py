class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=paragraph.lower()

        clean_str=paragraph.replace(","," ")
        clean_str=clean_str.replace("!"," ")
        clean_str=clean_str.replace("."," ")
        clean_str=clean_str.replace("?"," ")
        clean_str=clean_str.replace(";"," ")
        clean_str=clean_str.replace("'"," ")
        

        
        list_of=clean_str.split(" ")
        
        hashmap={}
        
        for i in list_of:
            if i not in banned and i!="":
                if i not in hashmap:
                    hashmap[i]=1
                else:
                    hashmap[i]+=1
        max_val=0
        for k,v in hashmap.items():
            if v>max_val:
                max_val=v
                ans=k
        return ans
      
