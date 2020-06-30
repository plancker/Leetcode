class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # Soln 2
        # if len(s) != len(t):
        #     return False
        # else:
        #     d = {}
        #     for i in s:
        #         if i in d.keys():
        #             d[i] = d[i]+1
        #         else:
        #             d[i] = 1
        #     for j in t:
        #         if j not in d.keys():
        #             return False
        #         else:
        #             if d[j] > 0:
        #                 d[j] = d[j]-1
        #             else:
        #                 return False
        #
        #     return True



X = Solution
print(X.isAnagram(X, "anakgram", "naggaram"))


