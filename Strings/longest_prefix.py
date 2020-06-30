class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        i = 0
        prefix = ""
        if len(strs)>0:
            while i < len(min(strs, key=len)) and [x[i] for x in strs] == [strs[0][i]]*len(strs):
                i = i+1
                prefix = strs[0][:i]
            return prefix
        return prefix


X = Solution
X.longestCommonPrefix(X, ["a"])