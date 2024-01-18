"""Tagged:C (LOL) """
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans=[]
        prev=s[0]
        count=1
        result=0
        for i in range(1,len(s)):
            if prev!=s[i]:
                prev=s[i]
                ans.append(count)
                count=1
            else:
                count+=1
        ans.append(count)

        for i in range(1,len(ans)):
            if ans[i-1]!=ans[i]:
                result+=min(ans[i-1],ans[i])
            else:
                result+=ans[i]
      
        return result