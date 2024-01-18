class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1: return str(strs[0])
        prev_ans=strs[0]     
        for i in range(1,len(strs)):
            ans=''
            str1=strs[i-1]
            str2=strs[i]
            min_len=min(len(str1),len(str2))
            for i in range(min_len):
                if str1[i]!=str2[i]:
                    break
                ans+=str1[i]
            if len(ans)<len(prev_ans):
                prev_ans=ans
        return prev_ans 
