class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans=[]

        # for word in words:
        #     for ele in word:
        #         if ele == x:
        #             ans.append(words.index(word))
        #             break
        # return ans

        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][j]==x:
                    ans.append(i)
                    break
        return ans

        
