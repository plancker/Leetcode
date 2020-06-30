class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums_set = set(nums)
        nums_dict = {}

        for i in range(len(nums)):
            if nums[i] in nums_dict.keys():
                nums_dict[nums[i]].append(i)
            else:
                nums_dict[nums[i]] = [i]

        for p in nums_set:
            q = target - p
            if q == p:
                if len(nums_dict[p]):
                    return nums_dict[p]
            if q in nums_set and q != p:
                k = [nums_dict[p][0], nums_dict[q][0]]
                k.sort()
                return k


X = Solution
print(X.twoSum(X,  [3,3], 6))