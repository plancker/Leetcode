class Solution:
    def maxSubArray(self, nums) -> int:

        k = {}

        def d((f, l)):
            if hash((f, l)) in k.keys():
                return k[hash((f, l))]
            else:
                if l - f == 1:
                    if sum(nums[f:l + 1]) > max(nums[f], nums[l]):
                        k[hash((f, l))] = sum(nums[f:l + 1])
                        return k[hash((f, l))]
                    elif nums[f] > max(sum(nums[f:l + 1]), nums[l]):
                        k[hash((f, f))] = nums[f]
                        return k[hash((f, f))]
                    elif nums[l] > max(sum(nums[f:l + 1]), nums[f]):
                        k[hash((l, l))] = nums[l]
                        return k[hash((l, l))]
                    else:
                        print("Hello")
                elif l - f == 0:
                    k[hash((f, f))] = nums[f]
                    return k[hash((f, f))]
                else:
                    # print(nums[f:l], nums[f + 1:l + 1])
                    m1 = d(f + 1, l)
                    m2 = d(f, l - 1)
                    if m1[0] == f + 1 and nums[f] > 0:
                        m1[0] = f
                    if m2[1] == l - 1 and nums[l] > 0:
                        m2[1] = l
                    m1_sum = sum(nums[m1[0]:m1[1] + 1])
                    m2_sum = sum(nums[m2[0]:m2[1] + 1])
                    if m1_sum > m2_sum:
                        return m1
                    else:
                        return m2

        m = d(nums)
        return m