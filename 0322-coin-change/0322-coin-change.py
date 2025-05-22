class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # Initialize dp array with infinity (amount + 1 is larger than any possible answer)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins to make amount 0
        
        # Build dp array for each amount from 1 to amount
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # If dp[amount] is still infinity, return -1; otherwise, return dp[amount]
        return dp[amount] if dp[amount] != float('inf') else -1