class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # nums.sort(key=lambda x: 0 if x != 0 else 100)

        i = 0
        seen = 0
        while seen < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            else:
                i = i+1
            seen = seen+1
        return nums


X = Solution
print(X.moveZeroes(X, []))
