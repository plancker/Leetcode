class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sl = [i for i in s.lower() if i.isalnum()]

        rsl = [i for i in reversed(sl)]

        if sl == rsl:
            return True
        else:
            return False

X = Solution
print(X.isPalindrome(X, ))
