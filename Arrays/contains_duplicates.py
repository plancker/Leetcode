class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        index = 1
        last = 0
        og_len = len(nums)

        nums.sort()

        while index < len(nums):
            if nums[index] == nums[last]:
                nums.pop(index)
            else:
                last = index
                index = index + 1

        if og_len > len(nums):
            return True
        else:
            return False


X = Solution
print(X.containsDuplicate(X, [1,2,3,1]))