class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:

        minn,pminn=float('inf'),float('inf')

        for price in prices:
            if price<minn:
                pminn=minn
                minn=price
            elif price<pminn:
                pminn=price
        summ=pminn+minn

        if summ<=money:
            return money-summ
        else:
            return money


"""
this is like 0/1 knapsack , atleast the idea is ... we calculate the last two mins and solve it in that way 

"""
