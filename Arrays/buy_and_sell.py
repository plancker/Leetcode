import numpy as np

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        print(prices)
        free = True
        # transactions = []
        sumt = 0
        last = None
        for t in range(len(prices)):
            if free:
                if t < len(prices) - 1 and prices[t] < prices[t + 1]:
                    # transactions.append(t)
                    last = t
                    free = False
            else:
                if t == len(prices) - 1:
                    # transactions.append(len(prices) - 1)
                    sumt = sumt + prices[t] - prices[last]
                    last = len(prices) - 1
                elif prices[t] > prices[t + 1]:
                    free = True
                    sumt = sumt + prices[t] - prices[last]
                    last = t
        return sumt


X = Solution
X.maxProfit(X,  np.random.randint(1, 100, 40))
