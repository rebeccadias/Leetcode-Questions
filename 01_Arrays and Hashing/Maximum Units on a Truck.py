class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
 
        boxTypes=sorted(boxTypes,key=lambda x:x[1],reverse=True)
        # print(boxTypes)
        answer=0
        for boxType in boxTypes:
            if truckSize>=boxType[0]:
                truckSize=truckSize-boxType[0]
                temp=boxType[0]*boxType[1]
                answer+=temp
            else:
                temp=boxType[1]*truckSize
                answer+=temp
                break
        return answer
