def isBadVersion(n):
    if n >= 1702766719:
        return True
    else:
        return False


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def fBVR(first, last):
            k = (first+last)//2
            if isBadVersion(k):
                if not isBadVersion(k - 1):
                    return k
                else:
                    return fBVR(first, k)
            else:
                if isBadVersion(k + 1):
                    return k + 1
                else:
                    return fBVR(k, last)

        return fBVR(1, n)

X = Solution
print(X.firstBadVersion(X, 2126753390))





