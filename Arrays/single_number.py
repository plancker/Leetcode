class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mset = set(nums)

        sum1 = 0
        sum2 = 0

        for i in mset:
            sum1 = sum1+i

        for j in nums:
            sum2 = sum2+j

        return 2*sum1 - sum2





X = Solution
print(X.singleNumber(X,  [4,1,2,1,2]))
