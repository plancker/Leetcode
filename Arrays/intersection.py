class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        nums_dict = {}
        intersection = []

        for i in nums1:
            if i in nums_dict.keys():
                nums_dict[i][0] = nums_dict[i][0]+1
            else:
                nums_dict[i] = [1,0]

        for j in nums2:
            if j in nums_dict.keys():
                nums_dict[j][1] = nums_dict[j][1]+1

        for t in nums_dict.keys():
            for i in range(min(nums_dict[t])):
                intersection.append(t)

        return intersection


X = Solution
print(X.intersect(X, [1,2,2,1], [2,1, 2,3,3]))




