def merge(nums1, m, nums2) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """

    def createSpace(j):
        for k in reversed(range(j, updated_m+1)):
            nums1[k] = nums1[k - 1]

    i = 0
    updated_m = m
    while len(nums2) > 0 and i < len(nums1):
        if nums2[0] < nums1[i]:
            createSpace(i)
            nums1[i] = nums2[0]
            nums2.pop(0)
            i = i + 1
            updated_m = updated_m+1
        else:
            i = i + 1

    if len(nums2) > 0:
        nums1[updated_m:updated_m+len(nums2)] = nums2

    return nums1


print(merge([1], 1, [], 0))
