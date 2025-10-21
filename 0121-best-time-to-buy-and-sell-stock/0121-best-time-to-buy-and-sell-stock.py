class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minimum = float('inf')
        best = 0

        for price in prices:
            if price < minimum:
                minimum = price

            else:
                best = max(best, price - minimum)

        return best
