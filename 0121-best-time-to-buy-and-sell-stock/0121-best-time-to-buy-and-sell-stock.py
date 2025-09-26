class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        best = 0
        least = float('inf')
        for price in prices:
            if price < least:
                least = price
            else:
                best = max(best,price - least)
        return best

