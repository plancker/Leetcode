class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        index = 1
        last = 0

        while index < len(nums):
            if nums[index] == nums[last]:
                nums.pop(index)
            else:
                last = index
                index = index + 1

        return len(nums)
        #
        # def remove_d(arr, index, last):
        #     if 0 < len(nums) != index and len(arr) > 0:
        #         if arr[index] == arr[last]:
        #             arr.pop(index)
        #             return remove_d(arr, index, last)
        #         else:
        #             last = index
        #             return remove_d(arr, index+1, last)
        #     else:
        #         return arr
        #
        # return len(remove_d(nums, 1, 0))


X = Solution
print(X.removeDuplicates(X,  [1,2,3,1]))

