class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float("inf")] * (amount+1) 
        # dp[i] == minimum number of coins to make i

        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if coin <= i:
                    # Try: every coin is the last coin
                    # ex:
                    # dp[6] = min(
                    #     dp[6-1] + 1,  # last coin = 1 (6-1)
                    #     dp[6-3] + 1,  # last coin = 3
                    #     dp[6-4] + 1   # last coin = 4
                    # )
                    # + 1 is counting current coin.
                    dp[i] = min(dp[i], dp[i-coin] + 1)
                    

        return dp[amount] if dp[amount] != float("inf") else -1