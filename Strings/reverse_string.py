class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for i in range(0, len(s)//2):
            temp = s[len(s)-(i+1)]
            s[len(s)-(i+1)] = s[i]
            s[i] = temp

        return s


X = Solution
print(X.reverseString(X,  ["h", "e", "l", "k"]))
