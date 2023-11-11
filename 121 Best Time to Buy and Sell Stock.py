class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        #checking if there is nothing in the list
        if len(prices)<2:
            return 0
        
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            # Update the minimum price if the current price is lower
            min_price = min(min_price, price)

            # Calculate the potential profit if selling at the current price
            potential_profit = price - min_price

            # Update the maximum profit if the potential profit is higher
            max_profit = max(max_profit, potential_profit)

        return max_profit
        
