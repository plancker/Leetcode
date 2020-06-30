class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        last = len(nums)-k
        temp = nums[:last]
        del nums[:last]
        nums.extend(temp)

        # j = 0
        # for i in range(last, len(nums)):
        #     temp = nums[i]
        #     nums[i] = nums[j]
        #     nums[j] = temp
        #     j = j+1

        return nums


X = Solution
print(X.rotate(X,  [-1], 2))
