"""my first dp """
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        dp=[0]*len(cost)

        dp[0]=cost[0]
        dp[1]=cost[1]
       
        for i in range(2,len(cost)):
            min_ele=min(dp[i-1],dp[i-2])
            dp[i]=cost[i]+min_ele         
        print(dp)
        return dp[-1]
