class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s != "":
            s_dict = {}
            for c in s:
                if c in s_dict.keys():
                    s_dict[c] = s_dict[c]+1
                else:
                    s_dict[c] = 0

            s_list = list(s)

            min = sorted(s_list, key=lambda x: s_dict[x])[0]

            if s_dict[min] > 0:
                return -1
            else:
                return s_list.index(min)
        else:
            return -1




X = Solution
print(X.firstUniqChar(X, ""))



