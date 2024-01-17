class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
    
        ans=[]
        products.sort()
        for i in range(len(searchWord)):
            temp = []
            searchString=searchWord[0:i+1]
            for product in products:
                if searchString == product[0:i+1]:
                    temp.append(product)
            products = temp
            ans.append(temp[:3])
        return ans
