class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        mstr = [str(k) for k in digits]
        mint = int("".join(mstr))
        mint = mint+1
        mint = [int(x) for x in str(mint)]

        return mint

X = Solution
print(X.plusOne(X, [0, 9,0,9]))
