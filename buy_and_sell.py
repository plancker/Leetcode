class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mi = prices[0]
        ma = prices[1]

        i = 2
        while i < len(prices)+1:
            mpt = i // 2
            mi = min(prices[0:mpt])
            ma = max(prices[mpt:i+1])
            i = i + 1

        return ma - mi

X = Solution
X.maxProfit(X, [7,1,5,3,6,4,32])